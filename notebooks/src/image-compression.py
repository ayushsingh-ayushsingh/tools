# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pillow",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Let's compress images

    Upload images, tune settings, compress images, then download results individually or as a ZIP.
    """)
    return


@app.cell
def _():
    import io
    import base64
    from pathlib import Path
    from typing import Any, BinaryIO, Optional, Union

    from PIL import Image, ImageOps

    LOSSY_FORMATS = {"JPEG", "JPG", "WEBP", "AVIF", "HEIF", "HEIC"}
    ALLOWED_FILETYPES = [".png", ".jpg", ".jpeg", ".webp", ".bmp"]

    RESAMPLE_FILTERS = {
        "nearest": Image.NEAREST,
        "box": Image.BOX,
        "bilinear": Image.BILINEAR,
        "hamming": Image.HAMMING,
        "bicubic": Image.BICUBIC,
        "lanczos": Image.LANCZOS,
    }

    ImageSource = Union[str, Path, bytes, bytearray, BinaryIO, Image.Image]
    ImageDestination = Union[str, Path, BinaryIO, None]

    def compress_image(
        input_source: ImageSource,
        output_path: ImageDestination = None,
        *,
        output_format: Optional[str] = None,
        quality: int = 80,
        lossless: bool = False,
        optimize: bool = True,
        progressive: bool = True,
        webp_method: int = 4,
        subsampling: Optional[Union[int, str]] = None,
        png_compress_level: int = 6,
        target_size_kb: Optional[float] = None,
        min_quality: int = 5,
        max_quality: int = 95,
        size_search_tolerance_kb: float = 2.0,
        resize_to: Optional[tuple[int, int]] = None,
        max_dimensions: Optional[tuple[int, int]] = None,
        scale_factor: Optional[float] = None,
        keep_aspect_ratio: bool = True,
        resample: Union[str, int] = "lanczos",
        upscale_if_smaller: bool = False,
        convert_mode: Optional[str] = None,
        reduce_colors: Optional[int] = None,
        grayscale: bool = False,
        background_color: tuple[int, int, int] = (255, 255, 255),
        strip_metadata: bool = True,
        preserve_exif: bool = False,
        preserve_icc_profile: bool = False,
        dpi: Optional[tuple[int, int]] = None,
        auto_orient: bool = True,
        return_stats: bool = True,
        verbose: bool = False,
    ) -> dict[str, Any]:
        original_bytes = read_original_bytes(input_source)
        img = open_image(input_source)
        original_dimensions = img.size

        if auto_orient:
            img = ImageOps.exif_transpose(img)

        exif_bytes = img.info.get("exif") if preserve_exif else None
        icc_bytes = (
            img.info.get("icc_profile") if preserve_icc_profile else None
        )

        resample_filter = (
            RESAMPLE_FILTERS.get(resample, resample)
            if isinstance(resample, str)
            else resample
        )
        img = apply_resize(
            img,
            resize_to=resize_to,
            max_dimensions=max_dimensions,
            scale_factor=scale_factor,
            keep_aspect_ratio=keep_aspect_ratio,
            resample_filter=resample_filter,
            upscale_if_smaller=upscale_if_smaller,
        )

        fmt = resolve_format(output_format, output_path, img)

        if grayscale:
            img = img.convert("L")

        if convert_mode:
            img = img.convert(convert_mode)
        elif fmt in {"JPEG", "JPG"} and img.mode in ("RGBA", "LA", "P"):
            img = flatten_alpha(img, background_color)
        elif fmt == "BMP" and img.mode not in ("RGB", "L", "P", "1"):
            img = img.convert("RGB")

        if reduce_colors:
            img = img.convert("RGB").quantize(
                colors=reduce_colors, method=Image.MEDIANCUT
            )

        def build_save_kwargs(q: int) -> dict[str, Any]:
            kwargs: dict[str, Any] = {"format": fmt, "optimize": optimize}

            if fmt in {"JPEG", "JPG"}:
                kwargs["quality"] = q
                kwargs["progressive"] = progressive
                if subsampling is not None:
                    kwargs["subsampling"] = resolve_subsampling(subsampling)
            elif fmt == "WEBP":
                kwargs["quality"] = q
                kwargs["lossless"] = lossless
                kwargs["method"] = webp_method
            elif fmt in {"AVIF", "HEIF", "HEIC"}:
                kwargs["quality"] = q
                kwargs["lossless"] = lossless
            elif fmt == "PNG":
                kwargs["compress_level"] = png_compress_level
                kwargs.pop("optimize", None)
                kwargs["optimize"] = optimize

            if dpi:
                kwargs["dpi"] = dpi
            if (
                exif_bytes
                and not strip_metadata
                or (exif_bytes and preserve_exif)
            ):
                kwargs["exif"] = exif_bytes
            if icc_bytes and (not strip_metadata or preserve_icc_profile):
                kwargs["icc_profile"] = icc_bytes

            return kwargs

        quality_used: Optional[int] = None
        if (
            target_size_kb is not None
            and fmt in LOSSY_FORMATS
            and not lossless
        ):
            encoded, quality_used = search_quality_for_target_size(
                img,
                build_save_kwargs,
                target_size_kb=target_size_kb,
                min_quality=min_quality,
                max_quality=max_quality,
                tolerance_kb=size_search_tolerance_kb,
            )
        else:
            quality_used = quality if fmt in LOSSY_FORMATS else None
            buffer = io.BytesIO()
            img.save(buffer, **build_save_kwargs(quality))
            encoded = buffer.getvalue()

        written_path: Optional[str] = None
        if output_path is not None:
            if isinstance(output_path, (str, Path)):
                with open(output_path, "wb") as f:
                    f.write(encoded)
                written_path = str(output_path)
            else:
                output_path.write(encoded)

        original_size = len(original_bytes)
        compressed_size = len(encoded)
        ratio = (compressed_size / original_size) if original_size else 0.0

        if verbose:
            print(
                f"[compress_image] {original_dimensions} -> {img.size} | "
                f"{fmt} | quality={quality_used} | "
                f"{original_size / 1024:.1f} KB -> {compressed_size / 1024:.1f} KB "
                f"({(1 - ratio) * 100:.1f}% saved)"
            )

        if not return_stats:
            return encoded

        stats: dict[str, Any] = {
            "original_size_bytes": original_size,
            "compressed_size_bytes": compressed_size,
            "compression_ratio": round(ratio, 4),
            "space_saved_percent": round((1 - ratio) * 100, 2),
            "original_dimensions": original_dimensions,
            "final_dimensions": img.size,
            "format": fmt,
            "quality_used": quality_used,
            "output_path": written_path,
        }
        if output_path is None:
            stats["data"] = encoded
        return stats

    def read_original_bytes(source: ImageSource) -> bytes:
        if isinstance(source, (bytes, bytearray)):
            return bytes(source)
        if isinstance(source, (str, Path)):
            with open(source, "rb") as f:
                return f.read()
        if isinstance(source, Image.Image):
            buf = io.BytesIO()
            fmt = source.format or "PNG"
            try:
                source.save(buf, format=fmt)
            except Exception:
                source.save(buf, format="PNG")
            return buf.getvalue()

        pos = source.tell() if hasattr(source, "tell") else None
        data = source.read()
        if pos is not None:
            source.seek(pos)
        return data

    def open_image(source: ImageSource) -> Image.Image:
        if isinstance(source, Image.Image):
            return source.copy()
        if isinstance(source, (bytes, bytearray)):
            return Image.open(io.BytesIO(source))
        if isinstance(source, (str, Path)):
            return Image.open(source)
        return Image.open(source)

    def apply_resize(
        img: Image.Image,
        *,
        resize_to,
        max_dimensions,
        scale_factor,
        keep_aspect_ratio,
        resample_filter,
        upscale_if_smaller,
    ) -> Image.Image:
        w, h = img.size

        if resize_to:
            target_w, target_h = resize_to
            if not upscale_if_smaller:
                target_w = min(target_w, w)
                target_h = min(target_h, h)
            if keep_aspect_ratio:
                img = ImageOps.contain(
                    img, (target_w, target_h), method=resample_filter
                )
            else:
                img = img.resize(
                    (target_w, target_h), resample=resample_filter
                )
            return img

        if max_dimensions:
            max_w, max_h = max_dimensions
            if upscale_if_smaller or w > max_w or h > max_h:
                img = ImageOps.contain(
                    img, (max_w, max_h), method=resample_filter
                )
            return img

        if scale_factor:
            if scale_factor < 1.0 or upscale_if_smaller:
                new_w = max(1, round(w * scale_factor))
                new_h = max(1, round(h * scale_factor))
                img = img.resize((new_w, new_h), resample=resample_filter)
            return img

        return img

    def resolve_format(output_format, output_path, img) -> str:
        if output_format:
            fmt = output_format.upper()
        elif isinstance(output_path, (str, Path)):
            ext = Path(output_path).suffix.lstrip(".").upper()
            fmt = ext if ext else (img.format or "JPEG")
        else:
            fmt = img.format or "JPEG"

        if fmt == "JPG":
            fmt = "JPEG"
        return fmt

    def flatten_alpha(
        img: Image.Image, background_color: tuple[int, int, int]
    ) -> Image.Image:
        if img.mode == "P":
            img = img.convert("RGBA")
        background = Image.new("RGB", img.size, background_color)
        if img.mode in ("RGBA", "LA"):
            background.paste(img, mask=img.split()[-1])
        else:
            background.paste(img)
        return background

    def resolve_subsampling(subsampling: Union[int, str]) -> int:
        if isinstance(subsampling, int):
            return subsampling
        mapping = {"4:4:4": 0, "4:2:2": 1, "4:2:0": 2}
        return mapping.get(subsampling, 2)

    def search_quality_for_target_size(
        img: Image.Image,
        build_save_kwargs,
        *,
        target_size_kb: float,
        min_quality: int,
        max_quality: int,
        tolerance_kb: float,
    ) -> tuple[bytes, int]:
        target_bytes = target_size_kb * 1024
        tolerance_bytes = tolerance_kb * 1024

        lo, hi = min_quality, max_quality
        best_encoded = None
        best_quality = lo

        while lo <= hi:
            mid = (lo + hi) // 2
            buffer = io.BytesIO()
            img.save(buffer, **build_save_kwargs(mid))
            encoded = buffer.getvalue()
            size = len(encoded)

            if abs(size - target_bytes) <= tolerance_bytes:
                return encoded, mid

            if size > target_bytes:
                hi = mid - 1
                if best_encoded is None or size < len(best_encoded):
                    best_encoded, best_quality = encoded, mid
            else:
                if best_encoded is None or (
                    len(best_encoded) > target_bytes
                    or size > len(best_encoded)
                ):
                    best_encoded, best_quality = encoded, mid
                lo = mid + 1

        if best_encoded is None:
            buffer = io.BytesIO()
            img.save(buffer, **build_save_kwargs(min_quality))
            best_encoded = buffer.getvalue()
            best_quality = min_quality

        return best_encoded, best_quality

    return ALLOWED_FILETYPES, compress_image


@app.cell
def _(mo):
    is_script_mode = mo.app_meta().mode == "script"
    return (is_script_mode,)


@app.cell
def _(ALLOWED_FILETYPES, mo):
    image_uploader = mo.ui.file(
        kind="area",
        label="Upload images to compress (you can select multiple)",
        filetypes=ALLOWED_FILETYPES,
        multiple=True,
    )
    image_uploader
    return (image_uploader,)


@app.cell
def _(image_uploader, is_script_mode):
    import io as _io

    from PIL import Image as _Image

    def _make_synthetic(name, size, color_a, color_b):
        img = _Image.new("RGB", size, color_a)
        px = img.load()
        w, h = size
        for x in range(w):
            for y in range(0, h, 4):
                if (x + y) % 8 == 0:
                    px[x, y] = color_b
        buf = _io.BytesIO()
        img.save(buf, format="PNG")
        return (name, buf.getvalue())

    if is_script_mode and not image_uploader.value:
        input_files = [
            _make_synthetic(
                "sample_red.png", (640, 480), (200, 60, 60), (60, 60, 200)
            ),
            _make_synthetic(
                "sample_green.png", (800, 600), (60, 180, 80), (240, 240, 240)
            ),
        ]
    else:
        input_files = [(f.name, f.contents) for f in image_uploader.value]
    return (input_files,)


@app.cell
def _(input_files):
    import io as _meta_io

    from PIL import Image as _MetaImage

    images_meta = []
    for _name, _data in input_files:
        try:
            with _MetaImage.open(_meta_io.BytesIO(_data)) as _im:
                _w, _h = _im.size
                _fmt = _im.format
        except Exception:
            _w, _h, _fmt = 0, 0, None
        images_meta.append(
            {
                "name": _name,
                "width": _w,
                "height": _h,
                "format": _fmt,
                "bytes": len(_data),
            }
        )

    _widths = [m["width"] for m in images_meta if m["width"] > 0]
    _heights = [m["height"] for m in images_meta if m["height"] > 0]
    max_w = max(_widths) if _widths else 1920
    max_h = max(_heights) if _heights else 1080
    return images_meta, max_h, max_w


@app.cell
def _(images_meta, input_files, mo):
    if not input_files:
        preview_ui = mo.md(
            "_No images uploaded yet. Use the upload area above (multiple files allowed)._"
        )
    else:
        _cards = []
        for _meta, (_fname, _fbytes) in zip(images_meta, input_files):
            _cards.append(
                mo.vstack(
                    [
                        mo.md(
                            f"**{_meta['name']}** — {_meta['width']}x{_meta['height']} "
                            f"({_meta['bytes'] / 1024:.1f} KB)"
                        ),
                        mo.image(
                            src=_fbytes,
                            rounded=True,
                            style={"maxWidth": "full", "height": "auto"},
                        ),
                    ]
                )
            )
        preview_ui = mo.vstack(
            [mo.md(f"## Uploaded images ({len(_cards)})"), *_cards], gap=4
        )
    preview_ui
    return


@app.cell
def _(max_h, max_w, mo):
    _eff_max_w = max(16, int(max_w))
    _eff_max_h = max(16, int(max_h))
    _default_max_w = min(1920, _eff_max_w)
    _default_max_h = min(1080, _eff_max_h)

    settings_form = (
        mo.md(
            """
            ## Compression settings

            Tweak everything, then press **Compress images**.
            Dimension sliders top out at your largest uploaded image
            (__MAXW__ x __MAXH__px).

            ## Output format & quality

            {output_format}

            {quality}

            {lossless}

            {optimize}

            {progressive}

            {webp_method}

            {subsampling}

            {png_compress_level}

            ## Target file size (optional)

            {enable_target_size}

            {target_size_kb}

            {min_quality}

            {max_quality}

            {tolerance_kb}

            ## Resize

            {resize_mode}

            {max_width}

            {max_height}

            {exact_width}

            {exact_height}

            {scale_factor}

            {keep_aspect_ratio}

            {resample}

            {upscale_if_smaller}

            ## Colors & background

            {convert_mode}

            {enable_reduce_colors}

            {reduce_colors}

            {grayscale}

            {bg_r}

            {bg_g}

            {bg_b}

            ## Metadata, DPI & orientation

            {strip_metadata}

            {preserve_exif}

            {preserve_icc_profile}

            {enable_dpi}

            {dpi}

            {auto_orient}
            """.replace("__MAXW__", str(_eff_max_w)).replace(
                "__MAXH__", str(_eff_max_h)
            )
        )
        .batch(
            output_format=mo.ui.dropdown(
                options=["JPEG", "PNG", "WEBP", "AVIF", "BMP"],
                value="WEBP",
                label="Output format (`output_format`)",
                allow_select_none=False,
            ),
            quality=mo.ui.slider(
                start=1,
                stop=100,
                step=1,
                value=85,
                label="Quality (`quality`)",
                show_value=True,
                debounce=True,
            ),
            lossless=mo.ui.checkbox(
                value=False, label="Lossless (`lossless`, WEBP/AVIF only)"
            ),
            optimize=mo.ui.checkbox(value=True, label="Optimize (`optimize`)"),
            progressive=mo.ui.checkbox(
                value=True, label="Progressive JPEG (`progressive`)"
            ),
            webp_method=mo.ui.slider(
                start=0,
                stop=6,
                step=1,
                value=4,
                label="WEBP method (`webp_method`, 0=fast … 6=slowest)",
                show_value=True,
            ),
            subsampling=mo.ui.dropdown(
                options=["default", "4:4:4", "4:2:2", "4:2:0"],
                value="default",
                label="JPEG chroma subsampling (`subsampling`, default = encoder default)",
                allow_select_none=False,
            ),
            png_compress_level=mo.ui.slider(
                start=0,
                stop=9,
                step=1,
                value=6,
                label="PNG compress level (`png_compress_level`)",
                show_value=True,
            ),
            enable_target_size=mo.ui.checkbox(
                value=False, label="Enable target file size (`target_size_kb`)"
            ),
            target_size_kb=mo.ui.slider(
                start=10,
                stop=5000,
                step=10,
                value=500,
                label="Target size in KB (`target_size_kb`)",
                show_value=True,
                debounce=True,
            ),
            min_quality=mo.ui.slider(
                start=1,
                stop=95,
                step=1,
                value=5,
                label="Min quality for size search (`min_quality`)",
                show_value=True,
            ),
            max_quality=mo.ui.slider(
                start=1,
                stop=100,
                step=1,
                value=95,
                label="Max quality for size search (`max_quality`)",
                show_value=True,
            ),
            tolerance_kb=mo.ui.slider(
                start=0.5,
                stop=50.0,
                step=0.5,
                value=5.0,
                label="Size search tolerance in KB (`size_search_tolerance_kb`)",
                show_value=True,
            ),
            resize_mode=mo.ui.radio(
                options=[
                    "none",
                    "max_dimensions",
                    "exact (resize_to)",
                    "scale_factor",
                ],
                value="max_dimensions",
                label="Resize mode",
            ),
            max_width=mo.ui.slider(
                start=1,
                stop=_eff_max_w,
                step=1,
                value=_default_max_w,
                label=f"Max width (`max_dimensions[0]`, caps at {_eff_max_w}px)",
                show_value=True,
                debounce=True,
            ),
            max_height=mo.ui.slider(
                start=1,
                stop=_eff_max_h,
                step=1,
                value=_default_max_h,
                label=f"Max height (`max_dimensions[1]`, caps at {_eff_max_h}px)",
                show_value=True,
                debounce=True,
            ),
            exact_width=mo.ui.slider(
                start=1,
                stop=_eff_max_w,
                step=1,
                value=_default_max_w,
                label=f"Exact width (`resize_to[0]`, caps at {_eff_max_w}px)",
                show_value=True,
                debounce=True,
            ),
            exact_height=mo.ui.slider(
                start=1,
                stop=_eff_max_h,
                step=1,
                value=_default_max_h,
                label=f"Exact height (`resize_to[1]`, caps at {_eff_max_h}px)",
                show_value=True,
                debounce=True,
            ),
            scale_factor=mo.ui.slider(
                start=0.05,
                stop=2.0,
                step=0.05,
                value=1.0,
                label="Scale factor (`scale_factor`)",
                show_value=True,
            ),
            keep_aspect_ratio=mo.ui.checkbox(
                value=True, label="Keep aspect ratio (`keep_aspect_ratio`)"
            ),
            resample=mo.ui.dropdown(
                options=[
                    "nearest",
                    "box",
                    "bilinear",
                    "hamming",
                    "bicubic",
                    "lanczos",
                ],
                value="lanczos",
                label="Resample filter (`resample`)",
                allow_select_none=False,
            ),
            upscale_if_smaller=mo.ui.checkbox(
                value=False, label="Upscale if smaller (`upscale_if_smaller`)"
            ),
            convert_mode=mo.ui.dropdown(
                options=["auto", "RGB", "RGBA", "L", "P"],
                value="auto",
                label="Convert mode (`convert_mode`, auto = None)",
                allow_select_none=False,
            ),
            enable_reduce_colors=mo.ui.checkbox(
                value=False, label="Enable color reduction (`reduce_colors`)"
            ),
            reduce_colors=mo.ui.slider(
                start=2,
                stop=256,
                step=1,
                value=128,
                label="Number of colors (`reduce_colors`)",
                show_value=True,
            ),
            grayscale=mo.ui.checkbox(
                value=False, label="Grayscale (`grayscale`)"
            ),
            bg_r=mo.ui.slider(
                start=0,
                stop=255,
                step=1,
                value=255,
                label="Background R (`background_color[0]`, JPEG flatten)",
                show_value=True,
            ),
            bg_g=mo.ui.slider(
                start=0,
                stop=255,
                step=1,
                value=255,
                label="Background G (`background_color[1]`)",
                show_value=True,
            ),
            bg_b=mo.ui.slider(
                start=0,
                stop=255,
                step=1,
                value=255,
                label="Background B (`background_color[2]`)",
                show_value=True,
            ),
            strip_metadata=mo.ui.checkbox(
                value=True, label="Strip metadata (`strip_metadata`)"
            ),
            preserve_exif=mo.ui.checkbox(
                value=False, label="Preserve EXIF (`preserve_exif`)"
            ),
            preserve_icc_profile=mo.ui.checkbox(
                value=False,
                label="Preserve ICC profile (`preserve_icc_profile`)",
            ),
            enable_dpi=mo.ui.checkbox(value=False, label="Enable DPI (`dpi`)"),
            dpi=mo.ui.slider(
                start=72,
                stop=600,
                step=1,
                value=300,
                label="DPI for x and y (`dpi`)",
                show_value=True,
            ),
            auto_orient=mo.ui.checkbox(
                value=True, label="Auto orient via EXIF (`auto_orient`)"
            ),
        )
        .form(
            submit_button_label="Compress images",
            show_clear_button=False,
            clear_on_submit=False,
            bordered=True,
        )
    )
    settings_form
    return (settings_form,)


@app.cell
def _(compress_image, input_files, max_h, max_w, mo, settings_form):
    import base64 as _b64
    import io as _out_io
    import json as _json
    import zipfile as _zipfile
    from pathlib import Path as _Path

    _s = settings_form.value or {}
    _submitted = settings_form.value is not None

    def _get(key, default):
        return _s.get(key, default) if isinstance(_s, dict) else default

    _def_max_w = min(1920, max(16, int(max_w)))
    _def_max_h = min(1080, max(16, int(max_h)))

    _output_format = _get("output_format", "WEBP")
    _quality = int(_get("quality", 85))
    _lossless = bool(_get("lossless", False))
    _optimize = bool(_get("optimize", True))
    _progressive = bool(_get("progressive", True))
    _webp_method = int(_get("webp_method", 4))
    _subsampling_raw = _get("subsampling", "default")
    _subsampling = None if _subsampling_raw == "default" else _subsampling_raw
    _png_level = int(_get("png_compress_level", 6))
    _use_target = bool(_get("enable_target_size", False))
    _target_kb = float(_get("target_size_kb", 500)) if _use_target else None
    _min_q = int(_get("min_quality", 5))
    _max_q = int(_get("max_quality", 95))
    _tol_kb = float(_get("tolerance_kb", 5.0))
    _resize_mode = _get("resize_mode", "max_dimensions")
    if _resize_mode == "max_dimensions":
        _resize_to = None
        _max_dims = (
            int(_get("max_width", _def_max_w)),
            int(_get("max_height", _def_max_h)),
        )
        _scale = None
    elif _resize_mode == "exact (resize_to)":
        _resize_to = (
            int(_get("exact_width", _def_max_w)),
            int(_get("exact_height", _def_max_h)),
        )
        _max_dims = None
        _scale = None
    elif _resize_mode == "scale_factor":
        _resize_to = None
        _max_dims = None
        _scale = float(_get("scale_factor", 1.0))
    else:
        _resize_to, _max_dims, _scale = None, None, None
    _keep_ar = bool(_get("keep_aspect_ratio", True))
    _resample = _get("resample", "lanczos")
    _upscale = bool(_get("upscale_if_smaller", False))
    _convert_raw = _get("convert_mode", "auto")
    _convert_mode = None if _convert_raw == "auto" else _convert_raw
    _use_reduce = bool(_get("enable_reduce_colors", False))
    _reduce_colors = int(_get("reduce_colors", 128)) if _use_reduce else None
    _grayscale = bool(_get("grayscale", False))
    _bg = (
        int(_get("bg_r", 255)),
        int(_get("bg_g", 255)),
        int(_get("bg_b", 255)),
    )
    _strip = bool(_get("strip_metadata", True))
    _keep_exif = bool(_get("preserve_exif", False))
    _keep_icc = bool(_get("preserve_icc_profile", False))
    _use_dpi = bool(_get("enable_dpi", False))
    _dpi_val = int(_get("dpi", 300))
    _dpi = (_dpi_val, _dpi_val) if _use_dpi else None
    _auto_orient = bool(_get("auto_orient", True))

    _fmt_ext = {
        "JPEG": "jpg",
        "PNG": "png",
        "WEBP": "webp",
        "AVIF": "avif",
        "BMP": "bmp",
    }
    _ext = _fmt_ext.get(
        str(_output_format).upper(), str(_output_format).lower()
    )

    compressed_results = []
    for _fname, _fbytes in input_files:
        try:
            _stats = compress_image(
                input_source=_fbytes,
                output_format=_output_format,
                quality=_quality,
                lossless=_lossless,
                optimize=_optimize,
                progressive=_progressive,
                webp_method=_webp_method,
                subsampling=_subsampling,
                png_compress_level=_png_level,
                target_size_kb=_target_kb,
                min_quality=_min_q,
                max_quality=_max_q,
                size_search_tolerance_kb=_tol_kb,
                resize_to=_resize_to,
                max_dimensions=_max_dims,
                scale_factor=_scale,
                keep_aspect_ratio=_keep_ar,
                resample=_resample,
                upscale_if_smaller=_upscale,
                convert_mode=_convert_mode,
                reduce_colors=_reduce_colors,
                grayscale=_grayscale,
                background_color=_bg,
                strip_metadata=_strip,
                preserve_exif=_keep_exif,
                preserve_icc_profile=_keep_icc,
                dpi=_dpi,
                auto_orient=_auto_orient,
                return_stats=True,
                verbose=False,
            )
            _stats["source_name"] = _fname
            _stem = _Path(_fname).stem or "image"
            _stats["download_name"] = f"optimized_{_stem}.{_ext}"
            _stats["error"] = None
        except Exception as _e:
            _stats = {
                "source_name": _fname,
                "download_name": _fname,
                "data": b"",
                "error": str(_e),
                "original_size_bytes": len(_fbytes),
                "compressed_size_bytes": 0,
                "space_saved_percent": 0.0,
                "original_dimensions": (0, 0),
                "final_dimensions": (0, 0),
                "format": _output_format,
                "quality_used": None,
            }
        compressed_results.append(_stats)

    _zip_buf = _out_io.BytesIO()
    _seen_names = set()
    with _zipfile.ZipFile(_zip_buf, "w", _zipfile.ZIP_DEFLATED) as _zf:
        for _r in compressed_results:
            if _r.get("error") or not _r.get("data"):
                continue
            _zname = _r["download_name"]
            _i = 1
            while _zname in _seen_names:
                _zname = f"{_Path(_r['download_name']).stem}_{_i}{_Path(_r['download_name']).suffix}"
                _i += 1
            _seen_names.add(_zname)
            _zf.writestr(_zname, _r["data"])
    zip_bytes = _zip_buf.getvalue()

    if not compressed_results:
        results_ui = mo.md(
            "_Upload images above, tune the settings form, then press **Compress images**._"
        )
    else:
        _status = (
            "Using your submitted settings."
            if _submitted
            else "Showing defaults, press **Compress images** to apply your settings."
        )
        _ok = [r for r in compressed_results if not r.get("error")]
        _total_orig = sum(
            r.get("original_size_bytes", 0) for r in compressed_results
        )
        _total_comp = sum(r.get("compressed_size_bytes", 0) for r in _ok)
        _saved = (1 - _total_comp / _total_orig) * 100 if _total_orig else 0.0
        _cards = [
            mo.md(
                f"### Compressed images ({len(_ok)}/{len(compressed_results)}) — "
                f"{_total_orig / 1024:.1f} KB → {_total_comp / 1024:.1f} KB "
                f"({_saved:.1f}% saved) · {_status}"
            )
        ]
        for _r in compressed_results:
            if _r.get("error"):
                _cards.append(
                    mo.vstack(
                        [
                            mo.md(
                                f"**{_r['source_name']}** — failed: `{_r['error']}`"
                            ),
                        ]
                    )
                )
                continue
            _cards.append(
                mo.vstack(
                    [
                        mo.md(
                            f"**{_r['source_name']}** → **{_r['download_name']}**  "
                            f"({_r['format']}, quality={_r['quality_used']})<br>"
                            f"Original: {_r['original_size_bytes'] / 1024:.1f} KB "
                            f"{_r['original_dimensions']} | Compressed: "
                            f"{_r['compressed_size_bytes'] / 1024:.1f} KB "
                            f"{_r['final_dimensions']} | Saved: {_r['space_saved_percent']}%"
                        ),
                        mo.image(
                            src=_r["data"],
                            rounded=True,
                            style={"maxWidth": "full", "height": "auto"},
                        ),
                        mo.download(
                            data=_r["data"],
                            filename=_r["download_name"],
                            label=f"Download \"{_r['download_name']}\"",
                        ),
                    ]
                )
            )
        if _ok:
            _cards.append(
                mo.download(
                    data=zip_bytes,
                    filename="compressed_images.zip",
                    mimetype="application/zip",
                    label=f"Download all {_ok.__len__()} image(s) as ZIP",
                )
            )
            _mime_by_ext = {
                "jpg": "image/jpeg",
                "jpeg": "image/jpeg",
                "png": "image/png",
                "webp": "image/webp",
                "avif": "image/avif",
                "bmp": "image/bmp",
            }
            _iframe_files = []
            for _r in _ok:
                _suffix = (
                    _Path(_r["download_name"]).suffix.lstrip(".").lower()
                )
                _iframe_files.append(
                    {
                        "name": _r["download_name"],
                        "mime": _mime_by_ext.get(
                            _suffix, "application/octet-stream"
                        ),
                        "b64": _b64.b64encode(_r["data"]).decode("ascii"),
                    }
                )
        results_ui = mo.vstack(_cards, gap=4)
    results_ui
    return


if __name__ == "__main__":
    app.run()

#!/usr/bin/env python3
"""Resize and trim GIFs so they play smoothly on the 320x240 screen.

Usage:
    python3 tools/gif_prep.py input.gif [more.gif ...] --out sdcard/gifs

To make a GIF from a video clip first (needs ffmpeg):
    ffmpeg -ss 5 -t 3 -i clip.mp4 -vf "fps=12,scale=240:-1" clip.gif
"""
import argparse
from pathlib import Path

from PIL import Image, ImageSequence


def prep(src: Path, out_dir: Path, size: int, fps: int, max_seconds: float) -> Path:
    with Image.open(src) as im:
        step = max(1, round(1000 / fps))  # target ms per frame
        frames, elapsed = [], 0
        for frame in ImageSequence.Iterator(im):
            if elapsed >= max_seconds * 1000:
                break
            rgb = frame.convert("RGB")
            rgb.thumbnail((size, size), Image.LANCZOS)
            frames.append(rgb.convert("P", palette=Image.ADAPTIVE, colors=128))
            elapsed += frame.info.get("duration", step)

        if not frames:
            raise ValueError(f"{src} has no frames")

        dest = out_dir / f"{src.stem}.gif"
        frames[0].save(
            dest,
            save_all=True,
            append_images=frames[1:],
            duration=step,
            loop=0,
            optimize=True,
        )
        return dest


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("inputs", nargs="+", type=Path)
    p.add_argument("--out", type=Path, default=Path("sdcard/gifs"))
    p.add_argument("--size", type=int, default=240, help="max width/height in pixels (default 240)")
    p.add_argument("--fps", type=int, default=12, help="output frames per second (default 12)")
    p.add_argument("--max-seconds", type=float, default=4.0, help="trim longer loops (default 4)")
    args = p.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    for src in args.inputs:
        dest = prep(src, args.out, args.size, args.fps, args.max_seconds)
        print(f"{src} -> {dest} ({dest.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

# 04 - GIF playback from the microSD card

Blocked by: 01

## What to build
Read a GIF file from the microSD card and play it in a loop on the screen. Use the AnimatedGIF library.

## Done when
- A GIF made with `tools/gif_prep.py` plays smoothly on the screen.
- The board shows a clear message when the card is missing or the file is not found.
- Write the real frame rate in this file. If it is too low, lower the default size or fps in `gif_prep.py`.

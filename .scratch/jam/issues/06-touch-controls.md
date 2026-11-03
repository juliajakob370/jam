# 06 - Touch controls

Blocked by: 03

## What to build
Use the resistive touchscreen to control playback:
- Tap the middle of the screen: play or pause.
- Tap the right edge: next track.
- Tap the left edge: previous track.

Use the XPT2046 touch chip on its own SPI bus. Add a touch calibration step.

## Done when
- All three taps work and do not trigger by mistake.
- Taps do not repeat when you hold your finger on the screen.
- Controls work when Spotify plays on another device.

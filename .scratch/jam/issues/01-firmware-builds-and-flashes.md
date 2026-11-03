# 01 - Firmware builds and flashes

Blocked by: none (needs the board)

## What to build
Flash the hello-world program to the board. Check that the screen and the BOOT button work.

## Done when
- `pio run` builds without errors.
- `pio run -t upload` flashes the board.
- The screen shows "jam".
- A green dot shows while you hold the BOOT button.
- If the colors look wrong, add the TFT_eSPI inversion flag to `platformio.ini`.

# Parts list (v1)

Budget: $50 max. Expected total: roughly $20–30.

| Part | Notes | Approx. price |
|---|---|---|
| ESP32-2432S028R "Cheap Yellow Display" | 2.8" 320x240 resistive touchscreen, WiFi, microSD slot, all on one board. **Check the title says S028R.** Other suffixes may have a different touch panel, and the firmware assumes resistive. Don't pay over about $20. | $8–20 |
| microSD card, 8–32 GB | Holds the GIFs and the playlist config. Any brand is fine. | $5–8 |
| USB cable that carries data | A charge-only cable can power the board but can't flash it. | $0–5 |
| USB power adapter | Any phone charger works, or plug into your computer. | $0 |
| Case (optional, deferred) | Some listings sell the board with a case included, at a small markup. Check the listing's variant selector. The library 3D printer is the other option. Confirm the case fits the S028R before buying. | $0–10 |

## Before you order

- 2.4 GHz WiFi is required. The ESP32 cannot join a 5 GHz-only network.
- A microSD card reader for your computer, if it has no slot.
- No soldering is needed for v1.

## Later (v2 ideas)

- External physical button wired to a spare GPIO pin.
- Battery power.
- Custom 3D-printed case.

# 02 - Setup wizard

Blocked by: none (does not need the board)

## What to build
Write an interactive script that guides you through the Spotify setup. It must:
- Open the Spotify developer page and tell you how to create an app.
- Ask for the Client ID and save it to `.env`.
- Run the one-time login and save the refresh token.
- Ask for the WiFi name and password and save them to `.env`.

Do not commit `.env`. It is in `.gitignore`.

## Done when
- You run the script once and `.env` has all four values.
- A test call to the Spotify "currently playing" endpoint works with the saved token.
- Re-running the script does not break the saved values.

# 05 - Playlist-to-GIF mapping

Blocked by: 03, 04

## What to build
Read a config file on the microSD card. It maps playlist IDs to GIF file names. When the playlist changes, the board plays the matching GIF. If no match exists, it plays the default GIF.

## Done when
- The config holds 5 to 10 playlists and one default.
- Changing the playlist in Spotify changes the GIF within a few seconds.
- Algorithmic playlists, albums and unknown playlists show the default GIF.
- A mistake in the config file shows an error message and does not crash the board.

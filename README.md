# GiantBomb Plex Media Server Agent

This is a [Plex Media Server] Agent to fetch metadata for downloaded [GiantBomb]
videos from their [API]. The user must provide his or her own API key in the
configuration options.

## File naming requirements

Currently the only reliable way to look up a video in the API is via its unique
ID, so the agent expects any downloaded file's name to begin with the ID (e.g.,
09313 - Quick Look Mount Your Friends.mp4)

## License

Copyright (c) 2014 Robert Speicher

Released under the MIT license. See `LICENSE` for more details.

[Plex Media Server]: https://plex.tv/
[GiantBomb]: http://www.giantbomb.com/
[API]: http://www.giantbomb.com/api/

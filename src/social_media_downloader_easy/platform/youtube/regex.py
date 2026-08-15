from pystandards.regex import RegularExpression

import re


class YoutubeVideoUrlkRegularExpression(
    RegularExpression
):
    """
    Regular expressions for Youtube video links.
    """

    YOUTUBE_VIDEO_ID_REGEX = r'[A-Za-z0-9_-]{11}'
    """
    The regular expression for the video ID part.
    """
    YOUTUBE_WATCH_REGEX = rf'^https?://(?:www\.)?youtube\.com/watch\?[^#]*?(?:^|&)v={YOUTUBE_VIDEO_ID_REGEX}(?:&|#|$)'
    """
    The long format including the full domain
    and the `watch?v` part.

    These are urls that will be detected:
    - https://www.youtube.com/watch?v=dQw4w9WgXcQ
    - https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s
    - https://www.youtube.com/watch?feature=share&v=dQw4w9WgXcQ
    """
    YOUTUBE_SHORT_URL_REGEX = rf'^https?://youtu\.be/{YOUTUBE_VIDEO_ID_REGEX}(?:[/?#]|$)'
    """
    The short format of the url that starts 
    with the `youtu.be` part.

    These are urls that will be detected:
    - https://youtu.be/dQw4w9WgXcQ
    - https://youtu.be/dQw4w9WgXcQ?t=30
    """
    YOUTUBE_SHORT_REGEX = rf'^https?://(?:www\.)?youtube\.com/shorts/{YOUTUBE_VIDEO_ID_REGEX}(?:[/?#]|$)'
    """
    The url of a short.

    These are urls that will be detected:
    - https://www.youtube.com/shorts/dQw4w9WgXcQ
    """
    YOUTUBE_EMBED_REGEX = rf'^https?://(?:www\.)?youtube(?:-nocookie)?\.com/embed/{YOUTUBE_VIDEO_ID_REGEX}(?:[/?#]|$)'
    """
    The url of an embed, that can be the official
    youtube or also the `youtube-nocookie` url.

    These are urls that will be detected:
    - https://www.youtube.com/embed/dQw4w9WgXcQ
    - https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ
    """
    YOUTUBE_V_REGEX = rf'^https?://(?:www\.)?youtube\.com/v/{YOUTUBE_VIDEO_ID_REGEX}(?:[/?#]|$)'
    """
    The full domain but with the `/v/` format.

    These are urls that will be detected:
    - https://www.youtube.com/v/dQw4w9WgXcQ
    """




# # From 'yta_youtube'
# YOUTUBE_VIDEO_ID = r'[0-9A-Za-z_-]{10}[048AEIMQUYcgkosw]'
# """
# The youtube video id regex.

# Based on this:
# https://webapps.stackexchange.com/questions/54443/format-for-id-of-youtube-video
# """
# YOUTUBE_CHANNEL_ID = r'[0-9A-Za-z_-]{21}[AQgw]'
# """
# The youtube channel id regex.

# Based on this:
# https://webapps.stackexchange.com/questions/54443/format-for-id-of-youtube-video
# """













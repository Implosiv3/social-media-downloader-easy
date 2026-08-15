from pystandards.enum import BaseEnumStr as Enum


class YoutubeUrlType(
    Enum
):
    
    WATCH = 'watch'
    SHORTS = 'shorts'
    SHORT_URL = 'short_url'
    EMBED = 'embed'
    V = 'v'
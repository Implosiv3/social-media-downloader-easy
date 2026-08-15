from enum import Enum


class FacebookUrlType(
    Enum
):
    
    WATCH = 'watch'
    VIDEO = 'video'
    REEL = 'reel'
    # TODO: Not working properly
    # SHORT_URL = 'short_url'
    SHARE_VIDEO = 'share_video'
    SHARE_REEL = 'share_reel'
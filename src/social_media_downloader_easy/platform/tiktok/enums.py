from pystandards.enum import BaseEnumStr as Enum


class TikTokUrlType(
    Enum
):

    # TODO: Rename to 'LONG_URL' instead (?)
    VIDEO = 'video'
    SHORT_URL = 'short_url'
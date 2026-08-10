from pystandards.regex import RegularExpression

import re


class TiktokVideoLinkRegularExpression(
    RegularExpression
):
    """
    Regular expressions for Instagram video links.
    """

    TIKTOK_VIDEO_LONG_REGEX = (
        r'https://(?:www\.)?tiktok\.com/'
        r'@(?P<username>[A-Za-z0-9._-]+)/'
        r'video/(?P<id>\d+)'
        r'(?:\?.*)?'
    )
    # TIKTOK_VIDEO_LONG_REGEX = r'https://www\.tiktok\.com/@(?P<username>[A-Za-z0-9._-]+)/video/(?P<id>\d+)(?:\?.*)?'
    TIKTOK_VIDEO_SHORT_REGEX = r'https://(?:www\.)?vm\.tiktok\.com/(?P<shareid>[A-Za-z0-9]+)'
    """
    TODO: This 'compile' below is failing because
    of the 'id':
    - re.error: redefinition of group name 'id' as group 2; was group 1 at position 108
    """
    # TIKTOK_GENERAL_REGEX = re.compile(
    #     '|'.join([
    #         TIKTOK_VIDEO_LONG_REGEX,
    #         TIKTOK_VIDEO_SHORT_REGEX,
    #     ])
    # )
    # """
    # The regex that includes all the accepted ones
    # together.
    # """

    #  TODO: Move this to 'GeneralRegularExpression' (?)
    @staticmethod
    def is_valid_url(
        url: str
    ):
        """
        Check if the `url` provided is accepted by
        any of our regular expressions or not.
        """
        return any(
            re.fullmatch(regex.value, url)
            for regex in TiktokVideoLinkRegularExpression
        )
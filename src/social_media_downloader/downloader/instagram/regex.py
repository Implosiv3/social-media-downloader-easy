from pystandards.regex import RegularExpression

import re


class InstagramVideoLinkRegularExpression(
    RegularExpression
):
    """
    Regular expressions for Instagram video links.
    """

    INSTAGRAM_REEL_REGEX  = r'https://(?:www\.)?instagram\.com/reel?/(?P<id>[a-zA-Z0-9_-]+)/?'
    INSTAGRAM_REELS_REGEX  = r'https://(?:www\.)?instagram\.com/reels?/(?P<id>[a-zA-Z0-9_-]+)/?'
    INSTAGRAM_SHARE_REGEX = r'https://(?:www\.)?instagram\.com/share/(?P<id>[a-zA-Z0-9_-]+)/?'
    INSTAGRAM_POST_REGEX  = r'https://(?:www\.)?instagram\.com/p/(?P<id>[a-zA-Z0-9_-]+)/?'
    """
    TODO: This 'compile' below is failing because
    of the 'id':
    - re.error: redefinition of group name 'id' as group 2; was group 1 at position 108
    """
    # INSTAGRAM_GENERAL_VIDEO_REGEX = re.compile(
    #     '|'.join([
    #         INSTAGRAM_REEL_REGEX,
    #         INSTAGRAM_REELS_REGEX,
    #         INSTAGRAM_SHARE_REGEX,
    #         INSTAGRAM_POST_REGEX,
    #     ])
    # )
    
    # The regex that includes all the accepted ones
    # together.
    

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
            for regex in InstagramVideoLinkRegularExpression
        )
"""
We have different types of valid urls:
# This one below doesn't include the ID
- 'https://www.facebook.com/share/r/1L6vVe9TjZ/'
- 'https://www.facebook.com/reel/875491608967954/'
- 'https://www.facebook.com/facebook/videos/875491608967954/'
- 'https://www.facebook.com/watch/?v=499831560618548'
- 'https://www.facebook.com/RolandGarros/videos/10155404760334920/FOO'
- 'https://www.facebook.com/RolandGarros/videos/FOO/10155404760334920'
"""
from pystandards.regex import RegularExpression

import re


class FacebookVideoLinkRegularExpression(
    RegularExpression
):
    """
    Regular expressions for Facebook video links.
    """
    FACEBOOK_SHARED_REEL_REGEX = r'https://www\.facebook\.com/share/r/[A-Za-z0-9]+/?'
    """
    This regular expression doesn't include the ID
    but an alphanumeric value that will redirect
    to the real video url.
    """
    # TODO: Add this (?P<id>) concept to pystandards.regex
    FACEBOOK_REEL_REGEX = r'https://www\.facebook\.com/reel/(?P<id>\d+)/?'
    FACEBOOK_VIDEO_REGEX = r'https://www\.facebook\.com/[^/]+/videos/(?P<id>\d+)/?'
    FACEBOOK_WATCH_REGEX = r'https://www\.facebook\.com/watch/\?v=(?P<id>\d+)'
    FACEBOOK_VIDEOS_SUFFIX_REGEX = r'https://www\.facebook\.com/[^/]+/videos/(?P<id>\d+)/[^/]+/?'
    FACEBOOK_VIDEOS_PREFIX_REGEX = r'https://www\.facebook\.com/[^/]+/videos/[^/]+/(?P<id>\d+)/?'
    """
    TODO: This 'compile' below is failing because
    of the 'id':
    - re.error: redefinition of group name 'id' as group 2; was group 1 at position 108
    """
    # FACEBOOK_GENERAL_VIDEO_REGEX = re.compile(
    #     '|'.join([
    #         FACEBOOK_SHARED_REEL_REGEX,
    #         FACEBOOK_REEL_REGEX,
    #         FACEBOOK_VIDEO_REGEX,
    #         FACEBOOK_WATCH_REGEX,
    #         FACEBOOK_VIDEOS_SUFFIX_REGEX,
    #         FACEBOOK_VIDEOS_PREFIX_REGEX,
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
            for regex in FacebookVideoLinkRegularExpression
        )
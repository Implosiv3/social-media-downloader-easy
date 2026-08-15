from pystandards.regex import RegularExpression


class FacebookPostUrlRegularExpression(
    RegularExpression
):
    """
    Regular expressions for Facebook video links.
    """

    FACEBOOK_POST_ID_REGEX = r"\d+"
    """
    The real Facebook video/reel ID.

    Examples:
    - 1234567890123456
    - 9876543210987654
    """

    FACEBOOK_SHORTCODE_REGEX = r"[A-Za-z0-9_-]+"
    """
    The shortcode used by Facebook short/share URLs.

    Examples:
    - abcDEF123
    - ZmAbC123
    """

    FACEBOOK_WATCH_URL_REGEX = (
        rf"^https?://(?:www\.|m\.)?facebook\.com/watch/"
        rf"\?(?:[^#]*&)?v=({FACEBOOK_POST_ID_REGEX})"
        rf"(?:&[^#]*)?(?:#.*)?$"
    )
    """
    Facebook Watch video URL, including the id.

    Examples:
    - https://www.facebook.com/watch/?v=1234567890123456
    - https://www.facebook.com/watch?v=1234567890123456
    - https://m.facebook.com/watch/?v=1234567890123456
    """

    FACEBOOK_VIDEO_URL_REGEX = (
        rf"^https?://(?:www\.|m\.)?facebook\.com/"
        rf"[^/?#]+/videos/"
        rf"({FACEBOOK_POST_ID_REGEX})"
        rf"(?:[/?#].*)?$"
    )
    """
    Facebook video URL belonging to a profile or
    page and including the id.

    Examples:
    - https://www.facebook.com/voyepic/videos/1234567890123456
    - https://www.facebook.com/somepage/videos/1234567890123456/
    - https://m.facebook.com/somepage/videos/1234567890123456
    """

    FACEBOOK_REEL_URL_REGEX = (
        rf"^https?://(?:www\.|m\.)?facebook\.com/reel/"
        rf"({FACEBOOK_POST_ID_REGEX})"
        rf"(?:[/?#].*)?$"
    )
    """
    Facebook Reel URL, including the id.

    Examples:
    - https://www.facebook.com/reel/1234567890123456
    - https://m.facebook.com/reel/1234567890123456/
    """

    # TODO: Not working properly
    # FACEBOOK_SHORT_URL_REGEX = (
    #     rf"^https?://fb\.watch/"
    #     rf"({FACEBOOK_SHORTCODE_REGEX})"
    #     rf"/?(?:[?#].*)?$"
    # )
    # """
    # Facebook short URL, including the shortcode.

    # Examples:
    # - https://fb.watch/abcDEF123/
    # - https://fb.watch/abcDEF123
    # """

    FACEBOOK_SHARE_VIDEO_URL_REGEX = (
        rf"^https?://(?:www\.|m\.)?facebook\.com/share/v/"
        rf"({FACEBOOK_SHORTCODE_REGEX})"
        rf"/?(?:[?#].*)?$"
    )
    """
    Facebook shared video URL, including the
    shortcode.

    Examples:
    - https://www.facebook.com/share/v/abcDEF123/
    - https://facebook.com/share/v/abcDEF123
    """

    FACEBOOK_SHARE_REEL_URL_REGEX = (
        rf"^https?://(?:www\.|m\.)?facebook\.com/share/r/"
        rf"({FACEBOOK_SHORTCODE_REGEX})"
        rf"/?(?:[?#].*)?$"
    )
    """
    Facebook shared Reel URL, including the
    shortcode.

    Examples:
    - https://www.facebook.com/share/r/abcDEF123/
    - https://facebook.com/share/r/abcDEF123
    """
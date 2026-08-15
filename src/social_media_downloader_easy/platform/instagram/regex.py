from pystandards.regex import RegularExpression


class InstagramPostUrlRegularExpression(
    RegularExpression
):
    """
    Regular expressions for Instagram video links.
    """

    INSTAGRAM_ID_REGEX = r'[A-Za-z0-9_-]+'
    """
    The id that identifies an Instagram post/reel.

    Examples:
    - DJx123ABC
    - CxYz_123
    """

    INSTAGRAM_REEL_URL_REGEX = (
        rf'^https?://(?:www\.)?instagram\.com/reel/'
        rf'({INSTAGRAM_ID_REGEX})/?(?:[?#].*)?$'
    )
    """
    The URL of an Instagram Reel.

    These are urls that will be detected:
    - https://www.instagram.com/reel/DJx123ABC/
    - https://instagram.com/reel/DJx123ABC
    - https://www.instagram.com/reel/DJx123ABC?igsh=abc
    """

    INSTAGRAM_POST_URL_REGEX = (
        rf'^https?://(?:www\.)?instagram\.com/p/'
        rf'({INSTAGRAM_ID_REGEX})/?(?:[?#].*)?$'
    )
    """
    The URL of an Instagram post.

    IMPORTANT:
    A `/p/` URL does not necessarily contain a video.
    It can contain an image, carousel, or video.

    These are urls that will be detected:
    - https://www.instagram.com/p/DJx123ABC/
    - https://instagram.com/p/DJx123ABC
    - https://www.instagram.com/p/DJx123ABC?igsh=abc
    """

    INSTAGRAM_REELS_URL_REGEX = (
        rf'^https?://(?:www\.)?instagram\.com/reels/'
        rf'({INSTAGRAM_ID_REGEX})/?(?:[?#].*)?$'
    )
    """
    Alternative Instagram Reel URL format.

    These are urls that will be detected:
    - https://www.instagram.com/reels/DJx123ABC/
    - https://www.instagram.com/reels/DJx123ABC?igsh=abc
    """

    INSTAGRAM_TV_URL_REGEX = (
        rf'^https?://(?:www\.)?instagram\.com/tv/'
        rf'({INSTAGRAM_ID_REGEX})/?(?:[?#].*)?$'
    )
    """
    Legacy Instagram IGTV URL format.

    These are urls that will be detected:
    - https://www.instagram.com/tv/DJx123ABC/
    """
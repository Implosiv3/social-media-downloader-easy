from pystandards.regex import RegularExpression



class TiktokPostUrlRegularExpression(
    RegularExpression
):
    """
    Regular expressions for Tiktok video links.
    """

    TIKTOK_POST_ID_REGEX = r"\d+"
    """
    The real video id, which is a long number that
    comes after the `/video/{id}` part.
    
    This one will come in a url like the following:
    - https://www.tiktok.com/@usuario/video/7512345678901234567
    """
    TIKTOK_SHORTCODE_REGEX = r"[A-Za-z0-9_-]+"
    """
    The redirect shortcode, which is an 
    alphanumerical value that will redirect you to
    the long format that includes the real id (the
    one for the `TIKTOK_POST_ID_REGEX`).

    This one will come in an url like the following:
    - https://vm.tiktok.com/ZMxxxxxx/
    """
    TIKTOK_POST_URL_REGEX = (
        rf'^https?://(?:www\.|m\.)?tiktok\.com/@([^/]+)/video/'
        rf'({TIKTOK_POST_ID_REGEX})(?:[/?#].*)?$'
    )
    """
    The long url that includes the username and
    the real video id.

    These are urls that will be detected:
    - https://www.tiktok.com/@user/video/1234567890123456789
    - https://tiktok.com/@user/video/1234567890123456789
    - https://m.tiktok.com/@user/video/1234567890123456789
    - https://www.tiktok.com/@user/video/1234567890123456789?is_from_webapp=1
    - https://www.tiktok.com/@user/video/1234567890123456789?_t=abc
    """
    TIKTOK_SHORT_URL_REGEX = (
        rf"^https?://(?:vm|vt)\.tiktok\.com/"
        rf"({TIKTOK_SHORTCODE_REGEX})/?(?:[?#].*)?$"
    )
    """
    The short url that will make a redirect to
    the long one. This one is including a
    shortcode but not the real video id nor the
    username.

    These are urls that will be detected:
    - https://vm.tiktok.com/ZMxxxxxx/
    - https://vm.tiktok.com/ZMxxxxxx
    - https://vt.tiktok.com/ZMxxxxxx/
    - https://vt.tiktok.com/ZMxxxxxx?foo=bar
    """
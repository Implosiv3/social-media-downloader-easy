from logging.handlers import WatchedFileHandler

from social_media_downloader_easy.platform.utils import get_url_from_redirecting_url
from social_media_downloader_easy.platform.facebook.regex import FacebookPostUrlRegularExpression


def share_facebook_url_to_long_facebook_url(
    url: str
) -> str:
    """
    Transform the sharing Facebook `url`
    provided the long format that includes
    the real post id.
    """
    return get_url_from_redirecting_url(
        url = url,
        regex = FacebookPostUrlRegularExpression.FACEBOOK_REEL_URL_REGEX
    )
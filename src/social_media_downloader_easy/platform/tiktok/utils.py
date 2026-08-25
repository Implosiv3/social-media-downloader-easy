from social_media_downloader_easy.platform.utils import get_url_from_redirecting_url
from social_media_downloader_easy.platform.tiktok.regex import TiktokPostUrlRegularExpression
from httpx_easy.client import HttpClient
from typing import Union

import re



def short_tiktok_url_to_long_tiktok_url(
    url: str
) -> str:
    """
    Transform the short Tiktok `url` provided
    to its long format that includes the
    username and the real video id.
    """
    # TODO: Should we validate it here (?)
    # if not TiktokPostUrlRegularExpression.TIKTOK_SHORT_URL_REGEX.is_valid(url):
    #     return None
    #     raise Exception('The "url" provided is not a short tiktok url.')
    
    with HttpClient(do_follow_redirects = True) as client:
        response = client.get.complete(
            url = url
        )
    
    return str(response.url)


def tiktok_video_id_to_long_tiktok_url(
    id: str
) -> str:
    """
    Obtain the long format url of the Tiktok
    video with the `id` provided.

    The `id` is only digits and its not
    the shortcode to share that comes in the
    short url.

    This method will navigate with a web
    scraper to get redirected and obtain the
    real url, and could need a captcha
    verification.
    """
    # TODO: Should we validate it here (?)
    # if not TiktokPostUrlRegularExpression.TIKTOK_POST_ID_REGEX.is_valid(id):
    #     return None
    #     raise Exception('The "id" provided is not a valid Tiktok video id.')

    """
    There is no way to obtain the real url
    by the response obtained. It has to be
    a web navigator that waits until the
    page is redirected to the real one.
    """

    url = f'https://www.tiktok.com/@/video/{id}'
    # This one below redirects to the one on top
    # url = f'https://tiktok.com/share/video/{id}'

    return get_url_from_redirecting_url(
        url = url,
        regex = TiktokPostUrlRegularExpression.TIKTOK_POST_URL_REGEX
        # https://www.tiktok.com/@voyepic/video/7669879089280339232
    )


def get_username_and_video_id_from_long_tiktok_url(
    url: str
) -> Union[tuple[str, str], None]:
    """
    Get the username and video id as a tuple
    from the Tiktok video long `url` provided.
    """
    # TODO: Should we validate it here (?)
    # if not TiktokPostUrlRegularExpression.TIKTOK_POST_URL_REGEX.is_valid(url):
    #     return None
    #     raise Exception('The "url" provided is not a valid Tiktok url.')
    
    match = re.fullmatch(TiktokPostUrlRegularExpression.TIKTOK_POST_URL_REGEX.value, url)

    return (
        match.group(1),
        match.group(2)
    )
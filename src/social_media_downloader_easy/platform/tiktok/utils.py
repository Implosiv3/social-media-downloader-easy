from social_media_downloader_easy.platform.tiktok.regex import TiktokVideoUrlRegularExpression
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
    if not TiktokVideoUrlRegularExpression.TIKTOK_SHORT_URL_REGEX.is_valid(url):
        raise Exception('The "url" provided is not a short tiktok url.')
    
    with HttpClient(do_follow_redirects = True) as client:
        response = client.get.complete(
            url = url
        )
    
    return str(response.url)


def get_username_and_video_id_from_long_tiktok_url(
    url: str
) -> Union[tuple[str, str], None]:
    """
    Get the username and video id as a tuple
    from the Tiktok video long `url` provided.
    """
    if not TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_URL_REGEX.is_valid(url):
        return None
    
    match = re.fullmatch(TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_URL_REGEX.value, url)

    return (
        match.group(1),
        match.group(2)
    )
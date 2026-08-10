"""
In this file we handle Tiktok url and we parse
them to obtain basic information and check if
they are valid ones or not.
"""
from social_media_downloader_easy.downloader.tiktok.regex import TiktokVideoLinkRegularExpression
from social_media_downloader_easy.downloader.tiktok.dataclasses import TiktokUrl
from social_media_downloader_easy.downloader.utils import clean_url
from httpx_easy.client import HttpClient

import re


class TiktokUrlParser:
    """
    Class to simplify the way we parse Tiktok
    videos urls.
    """


    @staticmethod
    def is_valid(
        url: str
    ) -> bool:
        """
        Check if the provided Tiktok video 'url' is
        valid or not.

        Check our accepted regex to know what urls
        are accepted.
        """
        return TiktokVideoLinkRegularExpression.is_valid_url(url)
    
    
    @staticmethod
    async def parse(
        url: str
    ) -> TiktokUrl:
        """
        Parse the provided `url` and return a TiktokUrl
        dataclass instance containing the author username,
        the video id and the long-format url, or raises
        an Exception if the given `url` is not valid.
        """
        if not TiktokUrlParser.is_valid(url):
            raise Exception('The provided "url" is not a valid Tiktok video url.')

        url = clean_url(url)
        # We need it long
        if not TiktokVideoLinkRegularExpression.TIKTOK_VIDEO_LONG_REGEX.is_valid(url):
            url = await _short_tiktok_url_to_long_tiktok_url(url)
            url = clean_url(url)

        id, username = _get_id_and_username_from_long_url(url)

        return TiktokUrl(
            username = username,
            video_id = id,
            url = url
        )



def _get_id_and_username_from_long_url(
    url: str
) -> TiktokUrl:
    """
    *For internal use only*

    Find the id and the username in the `url`
    given.
    """
    match = re.fullmatch(TiktokVideoLinkRegularExpression.TIKTOK_VIDEO_LONG_REGEX.value, url)

    if match:
        return (
            match.group('id'),
            match.group('username')
        )

    return None


async def _short_tiktok_url_to_long_tiktok_url(
    url: str
) -> str:
    """
    Transform the short Tiktok `url` provided
    to its long format.
    """
    if not TiktokVideoLinkRegularExpression.TIKTOK_VIDEO_SHORT_REGEX.is_valid_url(url):
        raise Exception('No "url" provided is not a short tiktok url.')
    
    async with HttpClient(do_follow_redirects = True) as client:
        response = await client.get.complete(
            url = url
        )
    
    return str(response.url)
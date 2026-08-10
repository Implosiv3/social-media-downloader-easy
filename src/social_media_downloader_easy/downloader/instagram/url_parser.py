"""
In this file we handle Facebook url and we parse
them to obtain basic information and check if
they are valid ones or not.

Here you have, by the way, some regular expressions
for the different instagram formats, extracted
from here:
- https://github.com/Okramjimmy/Instagram-reels-downloader/blob/c36c2055dc89f5028bdb99c9a9d689ea0affa175/src/features/instagram/utils.ts#L16-L18
"""
from social_media_downloader_easy.downloader.instagram.regex import InstagramVideoLinkRegularExpression
from social_media_downloader_easy.downloader.instagram.dataclasses import InstagramUrl
from social_media_downloader_easy.downloader.utils import clean_url

import re


class InstagramUrlParser:
    """
    Class to simplify the way we parse Instagram
    videos urls.
    """

    @staticmethod
    def is_valid(
        url: str
    ) -> bool:
        """
        Check if the provided Instagram video 'url' is
        valid or not.
        
        Check our accepted regex to know what urls
        are accepted.
        """
        return InstagramVideoLinkRegularExpression.is_valid_url(url)
    
    
    @staticmethod
    def parse(
        url: str
    ) -> InstagramUrl:
        """
        Parse the provided 'url' and return a InstagramUrl
        dataclass instance containing the author username,
        the video id and the long-format url, or raises
        an Exception if the given 'url' is not valid.
        """
        if not InstagramUrlParser.is_valid(url):
            raise Exception('The provided "url" is not a valid Instagram video url.')
        
        url = clean_url(url)
        id = _get_id_from_url(url)

        if not id:
            raise Exception('The "url" provided is valid but not supported because it does not include the real video id.')

        return InstagramUrl(
            video_id = id,
            url = url
        )



def _get_id_from_url(
    url: str
) -> InstagramUrl:
    """
    *For internal use only*

    Find the id of the video in the given `url`.
    """
    for regex in (
        InstagramVideoLinkRegularExpression.INSTAGRAM_SHARE_REGEX.value,
        InstagramVideoLinkRegularExpression.INSTAGRAM_POST_REGEX.value,
        InstagramVideoLinkRegularExpression.INSTAGRAM_REEL_REGEX.value,
    ):
        match = re.fullmatch(regex, url)

        if match:
            return match.group('id')

        return None


"""
Some urls just dropped:
- Short (shared reel): 'https://www.instagram.com/reel/DHQf6RmMFtf/?igsh=ZBDzeTA4cWkwbW4w'
"""
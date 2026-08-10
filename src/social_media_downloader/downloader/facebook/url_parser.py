"""
In this file we handle Facebook url and we parse
them to obtain basic information and check if
they are valid ones or not.

The id of a video, in Facebook, is numeric only.
If you shee numbers and letters is a sharing url
that will be transformed in the real id when
redirected.
"""
from social_media_downloader.downloader.facebook.dataclasses import FacebookUrl
from social_media_downloader.downloader.facebook.regex import FacebookVideoLinkRegularExpression
from social_media_downloader.downloader.utils import clean_url

import re


class FacebookUrlParser:
    """
    Class to simplify the way we parse Facebook
    videos urls.
    """

    @staticmethod
    def is_valid(
        url: str
    ) -> bool:
        """
        Check if the provided Facebook video `url`
        is valid or not.

        Check our accepted regex to know what urls
        are accepted.
        """
        return FacebookVideoLinkRegularExpression.is_valid_url(url)
    

    @staticmethod
    def parse(
        url: str
    ) -> FacebookUrl:
        """
        Parse the provided 'url' and return a FacebookUrl
        dataclass instance containing the video id and the
        short-format url, or raises an Exception if the
        given 'url' is not valid.
        """
        if not FacebookUrlParser.is_valid(url):
            raise Exception('The provided "url" is not a valid Facebook video url.')
        
        url = clean_url(url)
        id = _get_id_from_url(url)

        if not id:
            raise Exception('The "url" provided is valid but not supported because it does not include the real video id.')

        return FacebookUrl(
            video_id = id,
            url = url
        )



def _get_id_from_url(
    url: str
) -> FacebookUrl:
    """
    *For internal use only*

    Find the id of the video in the given `url`.
    """
    for regex in (
        FacebookVideoLinkRegularExpression.FACEBOOK_REEL_REGEX.value,
        FacebookVideoLinkRegularExpression.FACEBOOK_VIDEOS_REGEX.value,
        FacebookVideoLinkRegularExpression.FACEBOOK_WATCH_REGEX.value,
        FacebookVideoLinkRegularExpression.FACEBOOK_VIDEOS_SUFFIX_REGEX.value,
        FacebookVideoLinkRegularExpression.FACEBOOK_VIDEOS_PREFIX_REGEX.value,
    ):
        match = re.fullmatch(regex, url)

        if match:
            return match.group('id')

        return None
    
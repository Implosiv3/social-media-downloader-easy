from social_media_downloader_easy.platform.facebook.regex import FacebookPostUrlRegularExpression
from social_media_downloader_easy.platform.facebook.enums import FacebookUrlType
from social_media_downloader_easy.platform.facebook.utils import share_facebook_url_to_long_facebook_url
from dataclasses import dataclass, field
from typing import Union

import re


@dataclass
class FacebookPostUrl:
    """
    Dataclass to hold the information about
    a Facebook video URL.

    A Facebook video URL can have several formats.
    Some of them contain the real video ID directly,
    while others use a shortcode that must be resolved
    through a redirect.
    """

    url: str = field
    """
    The original URL provided when initializing
    the instance.
    """

    _url_type: FacebookUrlType = field(
        init = False
    )
    """
    *For internal use only*

    The original URL type this instance was
    built with.
    """

    _id: Union[str, None] = field(
        init = False,
        default = None,
        repr = False,
    )
    """
    *For internal use only*

    The Facebook video/reel ID.

    This is automatically extracted when the URL
    contains the real ID.
    """
    _long_url: Union[str, None] = field(
        init = False,
        default = None,
        repr = False
    )
    """
    *For internal use only*

    The long format url that includes the real
    post id.
    """

    @property
    def id(
        self
    ) -> Union[str, None]:
        """
        The Facebook video/reel ID.

        This is available immediately for URLs that
        contain the real ID.

        Short/share URLs require redirect resolution
        before the real ID can be obtained.
        """
        if self._id is None:
            self.long_url

        return self._id


    @property
    def long_url(
        self
    ) -> str:
        """
        The url in this format:
        - 'https://www.facebook.com/reel/{id}'
        """
        if self._long_url is not None:
            return self._long_url

        long_url = (
            share_facebook_url_to_long_facebook_url(self.url)
            if self._url_type in {
                # FacebookUrlType.SHORT_URL,
                FacebookUrlType.SHARE_VIDEO,
                FacebookUrlType.SHARE_REEL,
            } else
            self.url
        )

        id = _get_id_from_long_url(long_url)

        long_url = f'https://www.facebook.com/reel/{id}'

        self._long_url = long_url
        self._id = id

        return self._long_url
    

    @property
    def watch_url(
        self
    ) -> Union[str, None]:
        """
        Canonical Facebook Watch URL.

        The url in this format:
        - 'https://www.facebook.com/watch/?v={id}'
        """
        if self.id is None:
            self.long_url

        return f'https://www.facebook.com/watch/?v={self.id}'


    @property
    def reel_url(
        self
    ) -> Union[str, None]:
        """
        Canonical Facebook Reel URL.

        The url in this format:
        - 'https://www.facebook.com/reel/{id}'
        """
        if self.id is None:
            self.long_url

        return f'https://www.facebook.com/reel/{self.id}'


    def __post_init__(
        self
    ):
        # Autodetect the url type
        self._url_type = _get_url_type_from_url(self.url)

        # Autodetect long url and id
        # self.long_url


    @classmethod
    def from_id(
        cls,
        id: str
    ) -> 'FacebookPostUrl':
        """
        Get a FacebookPostUrl instance from a
        Facebook video/reel ID.
        """
        if not FacebookPostUrlRegularExpression.FACEBOOK_POST_ID_REGEX.is_valid(id):
            raise ValueError(f'Invalid Facebook video ID: {id}')

        return cls(
            url = f'https://www.facebook.com/watch/?v={id}'
        )


    @classmethod
    def from_shortcode(
        cls,
        shortcode: str
    ) -> 'FacebookPostUrl':
        """
        Get a FacebookPostUrl instance from a
        Facebook shortcode.

        The shortcode is used by fb.watch and share URLs.
        """
        if not FacebookPostUrlRegularExpression.FACEBOOK_SHORTCODE_REGEX.is_valid(shortcode):
            raise ValueError(f'Invalid Facebook shortcode: {shortcode}')

        return cls(
            url = f'https://www.facebook.com/share/v/{shortcode}/'
        )


    @classmethod
    def is_valid(
        cls,
        url: str
    ) -> bool:
        """
        Check if the URL provided is a valid Facebook
        video URL or not.
        """
        try:
            cls(url)
        except Exception as e:
            print(e)
            return False

        return True




def _get_url_type_from_url(
    url: str
) -> FacebookUrlType:
    """
    *For internal use only*

    Detect the URL type based on the original URL.
    """
    regex_type_dict = {
        FacebookPostUrlRegularExpression.FACEBOOK_WATCH_URL_REGEX: FacebookUrlType.WATCH,
        FacebookPostUrlRegularExpression.FACEBOOK_VIDEO_URL_REGEX: FacebookUrlType.VIDEO,
        FacebookPostUrlRegularExpression.FACEBOOK_REEL_URL_REGEX: FacebookUrlType.REEL,
        # FacebookPostUrlRegularExpression.FACEBOOK_SHORT_URL_REGEX: FacebookUrlType.SHORT_URL,
        FacebookPostUrlRegularExpression.FACEBOOK_SHARE_VIDEO_URL_REGEX: FacebookUrlType.SHARE_VIDEO,
        FacebookPostUrlRegularExpression.FACEBOOK_SHARE_REEL_URL_REGEX: FacebookUrlType.SHARE_REEL
    }

    for regex, type in regex_type_dict.items():
        if re.fullmatch(
            regex.value,
            url,
            re.IGNORECASE
        ):
            return type

    raise ValueError(f'Invalid Facebook URL: {url}')


def _get_id_from_long_url(
    url: str
) -> Union[str, None]:
    """
    *For internal use only*

    Get the id from the `url` provided that
    must be a long format that includes the
    id to be able to extract it.

    Short/share URLs only contain a
    shortcode, so in those cases the video
    ID remains None until the URL is
    resolved.
    """
    long_regex = [
        FacebookPostUrlRegularExpression.FACEBOOK_WATCH_URL_REGEX,
        FacebookPostUrlRegularExpression.FACEBOOK_VIDEO_URL_REGEX,
        FacebookPostUrlRegularExpression.FACEBOOK_REEL_URL_REGEX
    ]

    for regex in long_regex:
        match = re.fullmatch(
            regex.value,
            url,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

    return None

    if url_type == FacebookUrlType.WATCH:
        match = re.fullmatch(
            FacebookPostUrlRegularExpression.FACEBOOK_WATCH_URL_REGEX.value,
            url,
            re.IGNORECASE,
        )

        if match:
            return match.group(1)

    if url_type == FacebookUrlType.VIDEO:
        match = re.fullmatch(
            FacebookPostUrlRegularExpression.FACEBOOK_VIDEO_URL_REGEX.value,
            url,
            re.IGNORECASE,
        )

        if match:
            return match.group(1)

    if url_type == FacebookUrlType.REEL:
        match = re.fullmatch(
            FacebookPostUrlRegularExpression.FACEBOOK_REEL_URL_REGEX.value,
            url,
            re.IGNORECASE,
        )

        if match:
            return match.group(1)

    return None
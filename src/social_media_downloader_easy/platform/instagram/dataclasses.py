from social_media_downloader_easy.platform.instagram.regex import InstagramPostUrlRegularExpression
from social_media_downloader_easy.platform.instagram.enums import InstagramUrlType
from urllib.parse import urlparse
from dataclasses import dataclass, field
from typing import Union

import re


@dataclass
class InstagramPostUrl:
    """
    Dataclass to hold the information about
    an Instagram post url.
    """

    url: str = field
    """
    The original url provided when initializing
    the instance.
    """

    _url_type: InstagramUrlType = field(
        init = False
    )
    """
    *For internal use only*

    The original url type this instance was
    built with.
    """

    _id: Union[str, None] = field(
        init = False,
        default = None,
        repr = False,
    )
    """
    *For internal use only*

    The Instagram id autocalculated after
    being initialized.
    """

    @property
    def id(
        self
    ) -> str:
        """
        The id of the Instagram post/reel.
        """
        return self._id


    @property
    def long_url(
        self
    ) -> str:
        """
        The long url, a shortcut to the reel url.

        It is like this:
        - https://www.instagram.com/reel/{self.id}
        """
        return self.reel_url

    @property
    def reel_url(
        self
    ) -> str:
        """
        The url that uses the 'reel' prefix word.

        It is like this:
        - https://www.instagram.com/reel/{self.id}
        """
        return f'https://www.instagram.com/reel/{self.id}'


    @property
    def post_url(
        self
    ) -> str:
        """
        The url that uses the 'p' prefix word.

        It is like this:
        - https://www.instagram.com/p/{self.id}
        """
        return f'https://www.instagram.com/p/{self.id}'


    @property
    def reels_url(
        self
    ) -> str:
        """
        The url that uses the 'reels' prefix word.

        It is like this:
        - https://www.instagram.com/reels/{self.id}
        """
        return f'https://www.instagram.com/reels/{self.id}'


    @property
    def tv_url(
        self
    ) -> str:
        """
        The url that uses the 'tv' prefix word.

        It is like this:
        - https://www.instagram.com/tv/{self.id}
        """
        return f'https://www.instagram.com/tv/{self.id}'


    def __post_init__(
        self
    ):
        self._detect_url_type()
        self._extract_id()


    def _detect_url_type(
        self
    ) -> None:
        """
        *For internal use only*

        Detect the URL type based on the original URL.
        """
        if re.fullmatch(
            InstagramPostUrlRegularExpression.INSTAGRAM_REEL_URL_REGEX.value,
            self.url,
            re.IGNORECASE,
        ):
            self._url_type = InstagramUrlType.REEL
            return

        if re.fullmatch(
            InstagramPostUrlRegularExpression.INSTAGRAM_POST_URL_REGEX.value,
            self.url,
            re.IGNORECASE,
        ):
            self._url_type = InstagramUrlType.POST
            return

        if re.fullmatch(
            InstagramPostUrlRegularExpression.INSTAGRAM_REELS_URL_REGEX.value,
            self.url,
            re.IGNORECASE,
        ):
            self._url_type = InstagramUrlType.REELS
            return

        if re.fullmatch(
            InstagramPostUrlRegularExpression.INSTAGRAM_TV_URL_REGEX.value,
            self.url,
            re.IGNORECASE,
        ):
            self._url_type = InstagramUrlType.TV
            return

        raise ValueError(
            f'Invalid Instagram URL: {self.url}'
        )


    def _extract_id(
        self
    ) -> None:
        """
        *For internal use only*

        Extract the id from the URL.
        """
        parsed = urlparse(self.url)

        self._id = (
            parsed.path
            .strip('/')
            .split('/')[-1]
        )


    @classmethod
    def from_id(
        cls,
        id: str
    ) -> 'InstagramPostUrl':
        """
        Get an InstagramPostUrl instance from
        an Instagram id.
        """
        if not InstagramPostUrlRegularExpression.INSTAGRAM_ID_REGEX.is_valid(id):
            raise ValueError(f'Invalid Instagram id: {id}')

        return cls(
            url = f'https://www.instagram.com/reel/{id}/'
        )


    @classmethod
    def is_valid(
        cls,
        url: str
    ) -> bool:
        """
        Check if the url provided is a valid
        Instagram URL.
        """

        try:
            cls(url)
        except Exception as e:
            return False

        return True
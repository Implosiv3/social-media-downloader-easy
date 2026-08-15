from social_media_downloader_easy.platform.tiktok.regex import TiktokVideoUrlRegularExpression
from social_media_downloader_easy.platform.tiktok.utils import get_username_and_video_id_from_long_tiktok_url, short_tiktok_url_to_long_tiktok_url, tiktok_video_id_to_long_tiktok_url
from social_media_downloader_easy.platform.tiktok.enums import TikTokUrlType
from urllib.parse import urlparse
from dataclasses import dataclass, field
from typing import Union

import re



@dataclass
class TiktokVideoUrl:
    """
    Dataclass to hold the information about
    a TikTok video URL.

    A Tiktok video url will always have the
    long format version, but the short format
    depends on how it was instantiated.
    """

    url: str = field
    """
    The original url, that can be the long or
    the short format depending on what was
    provided when initializing the instance.

    Check the `.long_url` property for the
    long format.
    """

    _url_type: TikTokUrlType = field(
        init = False
    )
    """
    *For internal use only*

    The original url type this instance was
    built with.
    """
    _long_url: Union[str, None] = field(
        init = False,
        default = None,
        repr = False
    )
    """
    *For internal use only*

    The long format url without any additional
    information, including the username and
    the video id.
    """
    _username: Union[str, None] = field(
        init = False,
        default = None,
        repr = False,
    )
    """
    *For internal use only*

    The username autocalculated after being
    initialized.
    """
    _video_id: Union[str, None] = field(
        init = False,
        default = None,
        repr = False,
    )
    """
    *For internal use only*

    The video id autocalculated after being
    initialized.
    """

    @property
    def long_url(
        self
    ) -> str:
        if self._long_url is not None:
            return self._long_url

        # Resolve to long format
        long_url = (
            short_tiktok_url_to_long_tiktok_url(self.url)
            if self._url_type == TikTokUrlType.SHORT_URL else
            self.url
        )

        # Remove anything after ? if existing
        long_url = (
            long_url.split('?', 1)[0]
            if '?' in long_url else
            long_url
        )

        # Set metadata
        username, video_id = get_username_and_video_id_from_long_tiktok_url(long_url)

        self._username = username
        self._video_id = video_id
        self._long_url = long_url

        return self._long_url


    @property
    def username(
        self
    ) -> str:
        """
        The username of the Tiktok video url,
        that is based on the long format url
        of the video.
        """
        if self._username is None:
            # Force autodetection if needed
            self.long_url

        return self._username


    @property
    def video_id(
        self
    ) -> str:
        """
        The id of the Tiktok video, taht is
        based on its long format url.
        """
        if self._video_id is None:
            self.long_url

        return self._video_id


    def __post_init__(
        self
    ):
        self._detect_url_type()


    def _detect_url_type(
        self
    ) -> None:
        """
        *For internal use only*

        Detect the url type based on the `url`
        provided when initialized.
        """
        if re.fullmatch(
            TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_URL_REGEX.value,
            self.url,
            re.IGNORECASE,
        ):
            self._url_type = TikTokUrlType.VIDEO
            return

        match = re.fullmatch(
            TiktokVideoUrlRegularExpression.TIKTOK_SHORT_URL_REGEX.value,
            self.url,
            re.IGNORECASE,
        )

        if match:
            self._url_type = TikTokUrlType.SHORT_URL
            return

        raise ValueError(f'Invalid TikTok URL: {self.url}')
    

    # @classmethod
    # def parse(
    #     cls,
    #     url: str
    # ) -> Union['TiktokVideoUrl', None]:
    #     parsed = urlparse(url)

    #     if parsed.scheme not in ('http', 'https'):
    #         raise ValueError(f'Invalid TikTok URL scheme: {url}')

    #     hostname = (parsed.hostname or '').lower()
    #     path = parsed.path.rstrip('/')

    #     # ---------------------------------------------------------
    #     # Canonical:
    #     # https://www.tiktok.com/@username/video/123456789
    #     # ---------------------------------------------------------

    #     if hostname in {
    #         'tiktok.com',
    #         'www.tiktok.com',
    #         'm.tiktok.com',
    #     }:
    #         match = re.fullmatch(
    #             rf'/@[^/]+/video/({TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_ID_REGEX.value})',
    #             path,
    #         )

    #         if match:
    #             return cls(
    #                 video_id = match.group(1),
    #                 url_type = TikTokUrlType.VIDEO,
    #                 url = url,
    #             )

    #         return None

    #     # ---------------------------------------------------------
    #     # Short links:
    #     # https://vm.tiktok.com/Z...
    #     # https://vt.tiktok.com/Z...
    #     # ---------------------------------------------------------

    #     if hostname in {
    #         'vm.tiktok.com',
    #         'vt.tiktok.com',
    #     }:
    #         if path:
    #             return cls(
    #                 video_id = None,
    #                 url_type = TikTokUrlType.SHORT_URL,
    #                 url = url,
    #             )

    #         return None

    #     return None


    @classmethod
    def from_video_id(
        cls,
        video_id: str
    ) -> 'TiktokVideoUrl':
        """
        Get a `TiktokVideoUrl` instance of the Tiktok
        video with the `video_id` provided.
        """
        if not TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_ID_REGEX.is_valid(video_id):
            raise ValueError(f'Invalid Tiktok video ID: {video_id}')

        # We need to do a redirect in order to obtain
        # the long format url

        url = tiktok_video_id_to_long_tiktok_url(video_id)
        print(url)

        return cls(
            url = url,
        )


    @classmethod
    def from_shortcode(
        cls,
        shortcode: str
    ) -> 'TiktokVideoUrl':
        """
        Get a `TiktokVideoUrl` instance of the Tiktok
        video with the `shortcode` provided, which is
        the sharing shortcode.
        """
        if not TiktokVideoUrlRegularExpression.TIKTOK_SHORTCODE_REGEX.is_valid(shortcode):
            raise ValueError(f'Invalid Tiktok shortcode: {shortcode}')

        return cls(
            url = f'https://vm.tiktok.com/{shortcode}'
        )


    @classmethod
    def is_valid(
        cls,
        url: str
    ) -> bool:
        """
        Check if the `url` provided is valid Tiktok
        video url or not.
        """
        try:
            cls(url)
        except:
            return False

        return True

    """
    What if the video id is not valid and there
    is no video with that id? It means that the
    url will respond with a 404 or something...

    We should have a way to validate this.
    """


"""
- The link 'https://www.tiktok.com/@/video/7669879089280339232'
will solve on the redirect and find the username by itself.

- The link 'https://tiktok.com/share/video/7669879089280339232'
will solve on the redirect and find the username by itself.
"""

    
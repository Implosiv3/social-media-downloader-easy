from social_media_downloader_easy.platform.tiktok.regex import TiktokVideoUrlRegularExpression
from social_media_downloader_easy.platform.tiktok.utils import get_username_and_video_id_from_long_tiktok_url, short_tiktok_url_to_long_tiktok_url
from social_media_downloader_easy.platform.tiktok.enums import TikTokUrlType
from urllib.parse import urlparse
from dataclasses import dataclass, field
from typing import Union

import re



@dataclass(slots = True)
class TiktokVideoUrl:
    """
    Dataclass to hold the information about
    a TikTok video URL.

    A Tiktok video url will always have the
    long format version, but the short format
    depends on how it was instantiated.
    """

    video_id: Union[str, None]
    url_type: TikTokUrlType
    """
    The original url type this instance was
    built with.
    """
    url: str
    """
    The original url, that can be the long or
    the short format depending on what was
    provided when initializing the instance.

    Check the `.long_url` property for the
    long format.
    """
    _long_url: str = field(init = False, default = None)
    _username: str = field(init = False, default = None)

    @property
    def long_url(
        self
    ) -> str:
        if not hasattr(self, '_long_url'):
            long_url = (
                short_tiktok_url_to_long_tiktok_url(self.url)
                if self.url_type == TikTokUrlType.SHORT_URL else
                self.url
            )

            # Remove anything after ? if existing due to redirect
            long_url = (
                long_url.split('?', 1)[0]
                if '?' in long_url else
                long_url
            )
            username, video_id = get_username_and_video_id_from_long_tiktok_url(long_url)

            self._long_url = long_url
            self._username = username
            self.video_id = video_id

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
        if not hasattr(self, '_username'):
            match = re.match(
                TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_URL_REGEX.value,
                self.long_url,
                re.IGNORECASE
            )

            if not match:
                raise ValueError(
                    f'Invalid TikTok long URL: {self._long_url}'
                )

            self._username: str = match.group(1)

        return self._username


    def __post_init__(
        self
    ):
        # Validate type
        TikTokUrlType.to_enum(self.url_type)
    

    @classmethod
    def parse(
        cls,
        url: str
    ) -> Union['TiktokVideoUrl', None]:
        parsed = urlparse(url)

        if parsed.scheme not in ('http', 'https'):
            raise ValueError(f'Invalid TikTok URL scheme: {url}')

        hostname = (parsed.hostname or '').lower()
        path = parsed.path.rstrip('/')

        # ---------------------------------------------------------
        # Canonical:
        # https://www.tiktok.com/@username/video/123456789
        # ---------------------------------------------------------

        if hostname in {
            'tiktok.com',
            'www.tiktok.com',
            'm.tiktok.com',
        }:
            match = re.fullmatch(
                rf'/@[^/]+/video/({TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_ID_REGEX.value})',
                path,
            )

            if match:
                return cls(
                    video_id = match.group(1),
                    url_type = TikTokUrlType.VIDEO,
                    url = url,
                )

            return None

        # ---------------------------------------------------------
        # Short links:
        # https://vm.tiktok.com/Z...
        # https://vt.tiktok.com/Z...
        # ---------------------------------------------------------

        if hostname in {
            'vm.tiktok.com',
            'vt.tiktok.com',
        }:
            if path:
                return cls(
                    video_id = None,
                    url_type = TikTokUrlType.SHORT_URL,
                    url = url,
                )

            return None

        return None


    @classmethod
    def from_video_id(
        cls,
        video_id: str
    ) -> 'TiktokVideoUrl':
        if not TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_ID_REGEX.is_valid(video_id):
            raise ValueError(f'Invalid TikTok video ID: {video_id}')

        return cls(
            video_id = video_id,
            url_type = TikTokUrlType.VIDEO,
            url = f'https://www.tiktok.com/video/{video_id}',
        )

    
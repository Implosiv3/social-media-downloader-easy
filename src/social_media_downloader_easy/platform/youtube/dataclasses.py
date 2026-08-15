from social_media_downloader_easy.platform.youtube.regex import YoutubeVideoUrlRegularExpression
from social_media_downloader_easy.platform.youtube.enums import YoutubeUrlType
from dataclasses import dataclass, field
from urllib.parse import parse_qs, urlparse
from typing import Union

import re


@dataclass
class YoutubeVideoUrl:
    """
    Class to handle a Youtube video url and
    also parse or validate them.
    """

    url: str = field
    """
    The original url that was provided when
    initializing the instance.
    """

    _url_type: YoutubeUrlType = field(
        init = False
    )
    """
    *For internal use only*

    The original url type this instance was
    built with.
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
    def watch_url(
        self
    ) -> str:
        """
        The long format of the Youtube video.

        It is like this:
        - https://www.youtube.com/watch?v={video_id}
        """
        return f'https://www.youtube.com/watch?v={self._video_id}'


    @property
    def v_url(
        self
    ) -> str:
        """
        Another format with the '/v/' in the
        middle.

        It is like this:
        - https://www.youtube.com/v/{video_id}
        """
        return f'https://www.youtube.com/v/{self._video_id}'
    

    @property
    def short_url(
        self
    ) -> str:
        """
        The short format of the Youtube video.

        It is like this:
        - https://youtu.be/{video_id}
        """
        return f'https://youtu.be/{self._video_id}'


    @property
    def shorts_url(
        self
    ) -> str:
        """
        The url of the video for the shorts
        section.

        It is like this:
        - https://www.youtube.com/shorts/{video_id}
        """
        return f'https://www.youtube.com/shorts/{self._video_id}'


    @property
    def embed_url(
        self
    ) -> str:
        """
        The url to embed the Youtube video or
        short.

        It is like this:
        - `https://www.youtube.com/embed/{video_id}`
        """
        return f'https://www.youtube.com/embed/{self._video_id}'


    @property
    def embed_nocookie_url(
        self
    ) -> str:
        """
        The url to embed the Youtube video or
        short through the nocookie service.

        It is like this:
        - `https://youtube-nocookie.com/embed/{video_id}`
        """
        return f'https://youtube-nocookie.com/embed/{self._video_id}'


    @property
    def thumbnail_url(
        self
    ) -> str:
        """
        The direct url to get the thumbnail.

        It is like this:
        - https://img.youtube.com/vi/{video_id}/oardefault.jpg
        """
        return f'https://img.youtube.com/vi/{self._video_id}/oardefault.jpg'


    @property
    def video_id(
        self
    ) -> str:
        """
        The id of the video.
        """
        return self._video_id


    def __post_init__(
        self
    ):
        self._detect_url_type()
        self._extract_video_id()


    def _detect_url_type(
        self
    ) -> str:
        """
        *For internal use only*

        Detect the url type based on the `url`
        provided when initialized.
        """
        if re.match(
            YoutubeVideoUrlRegularExpression.YOUTUBE_WATCH_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.WATCH
            return

        if re.match(
            YoutubeVideoUrlRegularExpression.YOUTUBE_SHORT_URL_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.SHORT_URL
            return

        if re.match(
            YoutubeVideoUrlRegularExpression.YOUTUBE_SHORTS_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.SHORTS
            return

        if re.match(
            YoutubeVideoUrlRegularExpression.YOUTUBE_EMBED_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.EMBED
            return

        if re.match(
            YoutubeVideoUrlRegularExpression.YOUTUBE_V_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.V
            return

        raise ValueError(f'Unsupported Youtube video url: {self.url}')


    def _extract_video_id(
        self
    ) -> None:
        """
        *For internal use only*

        Extract the video id from the original URL.
        """
        if self._url_type == YoutubeUrlType.WATCH:
            self._video_id = parse_qs(
                urlparse(self.url).query
            )['v'][0]
            return

        if self._url_type == YoutubeUrlType.SHORT_URL:
            self._video_id = urlparse(self.url).path.strip('/').split('/')[0]
            return

        if self._url_type == YoutubeUrlType.SHORTS:
            self._video_id = urlparse(self.url).path.strip('/').split('/')[1]
            return

        if self._url_type == YoutubeUrlType.EMBED:
            self._video_id = urlparse(self.url).path.strip('/').split('/')[1]
            return

        if self._url_type == YoutubeUrlType.V:
            self._video_id = urlparse(self.url).path.strip('/').split('/')[1]
            return

        raise ValueError(f'Unsupported Youtube url type: {self._url_type}')


    @classmethod
    def from_video_id(
        cls,
        video_id: str
    ) -> 'YoutubeVideoUrl':
        """
        Get the `YoutubeVideoUrl` instance that
        includes the `video_id` provided, if
        valid.
        """
        if not YoutubeVideoUrlRegularExpression.YOUTUBE_VIDEO_ID_REGEX.is_valid(video_id):
            raise ValueError(f'Invalid YouTube video id: {video_id}')

        url = f'https://www.youtube.com/watch?v={video_id}'

        return cls(
            url = url
        )


    # @classmethod
    # def parse(
    #     cls,
    #     url: str
    # ) -> Union['YoutubeVideoUrl', None]:
    #     """
    #     Parse the Youtube `url` provided and return
    #     a `YoutubeVideoUrl` instance if parseable.

    #     This method is accepting:
    #     - https://www.youtube.com/watch?v=dQw4w9WgXcQ
    #     - https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s
    #     - https://www.youtube.com/watch?feature=share&v=dQw4w9WgXcQ
    #     - https://youtu.be/dQw4w9WgXcQ
    #     - https://youtu.be/dQw4w9WgXcQ?t=30
    #     - https://www.youtube.com/shorts/dQw4w9WgXcQ
    #     - https://www.youtube.com/embed/dQw4w9WgXcQ
    #     - https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ
    #     - https://www.youtube.com/v/dQw4w9WgXcQ
    #     """
    #     parsed = urlparse(url)

    #     if parsed.scheme not in ('http', 'https'):
    #         return None

    #     hostname = parsed.hostname
    #     if hostname is None:
    #         return None

    #     hostname = hostname.lower()

    #     # youtu.be/VIDEO_ID
    #     if hostname == 'youtu.be':
    #         video_id = parsed.path.strip('/').split('/')[0]

    #         if YoutubeVideoUrlRegularExpression.YOUTUBE_VIDEO_ID_REGEX.fullmatch(video_id, re.IGNORECASE):
    #             return cls(
    #                 video_id = video_id,
    #                 url_type = YoutubeUrlType.SHORT_URL,
    #             )

    #         return None

    #     # youtube.com / www.youtube.com / youtube-nocookie.com
    #     if hostname not in {
    #         'youtube.com',
    #         'www.youtube.com',
    #         'youtube-nocookie.com',
    #         'www.youtube-nocookie.com',
    #     }:
    #         return None

    #     path = parsed.path.rstrip('/')

    #     # /watch?v=VIDEO_ID
    #     if path == '/watch':
    #         video_id = parse_qs(parsed.query).get('v', [None])[0]

    #         if (
    #             video_id and
    #             YoutubeVideoUrlRegularExpression.YOUTUBE_VIDEO_ID_REGEX.fullmatch(video_id, re.IGNORECASE)
    #         ):
    #             return cls(
    #                 video_id = video_id,
    #                 url_type = YoutubeUrlType.WATCH,
    #             )

    #         return None

    #     # /shorts/VIDEO_ID
    #     match = re.fullmatch(
    #         rf'/shorts/({YoutubeVideoUrlRegularExpression.YOUTUBE_VIDEO_ID_REGEX.value})',
    #         path,
    #         re.IGNORECASE
    #     )

    #     if match:
    #         return cls(
    #             video_id = match.group(1),
    #             url_type = YoutubeUrlType.SHORTS,
    #         )

    #     # /embed/VIDEO_ID
    #     match = re.fullmatch(
    #         rf'/embed/({YoutubeVideoUrlRegularExpression.YOUTUBE_VIDEO_ID_REGEX.value})',
    #         path,
    #         re.IGNORECASE
    #     )

    #     if match:
    #         return cls(
    #             video_id = match.group(1),
    #             url_type = YoutubeUrlType.EMBED,
    #         )

    #     # /v/VIDEO_ID
    #     match = re.fullmatch(
    #         rf'/v/({YoutubeVideoUrlRegularExpression.YOUTUBE_VIDEO_ID_REGEX.value})',
    #         path,
    #         re.IGNORECASE
    #     )

    #     if match:
    #         return cls(
    #             video_id = match.group(1),
    #             url_type = YoutubeUrlType.V,
    #         )

    #     return None


    @classmethod
    def is_valid(
        cls,
        url: str
    ) -> bool:
        """
        Check if the `url` provided is valid Youtube
        video url or not.
        """
        try:
            cls(url)
        except Exception as e:
            return False

        return True
from social_media_downloader_easy.platform.youtube.regex import YoutubePostUrlRegularExpression
from social_media_downloader_easy.platform.youtube.enums import YoutubeUrlType
from dataclasses import dataclass, field
from urllib.parse import parse_qs, urlparse
from typing import Union

import re


@dataclass
class YoutubePostUrl:
    """
    Class to handle a Youtube post url and
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
    _id: Union[str, None] = field(
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
        - https://www.youtube.com/watch?v={id}
        """
        return f'https://www.youtube.com/watch?v={self._id}'


    @property
    def v_url(
        self
    ) -> str:
        """
        Another format with the '/v/' in the
        middle.

        It is like this:
        - https://www.youtube.com/v/{id}
        """
        return f'https://www.youtube.com/v/{self._id}'
    

    @property
    def short_url(
        self
    ) -> str:
        """
        The short format of the Youtube video.

        It is like this:
        - https://youtu.be/{id}
        """
        return f'https://youtu.be/{self._id}'


    @property
    def shorts_url(
        self
    ) -> str:
        """
        The url of the video for the shorts
        section.

        It is like this:
        - https://www.youtube.com/shorts/{id}
        """
        return f'https://www.youtube.com/shorts/{self._id}'


    @property
    def embed_url(
        self
    ) -> str:
        """
        The url to embed the Youtube video or
        short.

        It is like this:
        - `https://www.youtube.com/embed/{id}`
        """
        return f'https://www.youtube.com/embed/{self._id}'


    @property
    def embed_nocookie_url(
        self
    ) -> str:
        """
        The url to embed the Youtube video or
        short through the nocookie service.

        It is like this:
        - `https://youtube-nocookie.com/embed/{id}`
        """
        return f'https://youtube-nocookie.com/embed/{self._id}'


    @property
    def thumbnail_url(
        self
    ) -> str:
        """
        The direct url to get the thumbnail.

        It is like this:
        - https://img.youtube.com/vi/{id}/oardefault.jpg
        """
        return f'https://img.youtube.com/vi/{self._id}/oardefault.jpg'


    @property
    def id(
        self
    ) -> str:
        """
        The id of the video.
        """
        return self._id


    def __post_init__(
        self
    ):
        self._detect_url_type()
        self._extract_id()


    def _detect_url_type(
        self
    ) -> str:
        """
        *For internal use only*

        Detect the url type based on the `url`
        provided when initialized.
        """
        if re.match(
            YoutubePostUrlRegularExpression.YOUTUBE_WATCH_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.WATCH
            return

        if re.match(
            YoutubePostUrlRegularExpression.YOUTUBE_SHORT_URL_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.SHORT_URL
            return

        if re.match(
            YoutubePostUrlRegularExpression.YOUTUBE_SHORTS_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.SHORTS
            return

        if re.match(
            YoutubePostUrlRegularExpression.YOUTUBE_EMBED_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.EMBED
            return

        if re.match(
            YoutubePostUrlRegularExpression.YOUTUBE_V_REGEX.value,
            self.url,
        ):
            self._url_type = YoutubeUrlType.V
            return

        raise ValueError(f'Unsupported Youtube post url: {self.url}')


    def _extract_id(
        self
    ) -> None:
        """
        *For internal use only*

        Extract the id from the original URL.
        """
        if self._url_type == YoutubeUrlType.WATCH:
            self._id = parse_qs(
                urlparse(self.url).query
            )['v'][0]
            return

        if self._url_type == YoutubeUrlType.SHORT_URL:
            self._id = urlparse(self.url).path.strip('/').split('/')[0]
            return

        if self._url_type == YoutubeUrlType.SHORTS:
            self._id = urlparse(self.url).path.strip('/').split('/')[1]
            return

        if self._url_type == YoutubeUrlType.EMBED:
            self._id = urlparse(self.url).path.strip('/').split('/')[1]
            return

        if self._url_type == YoutubeUrlType.V:
            self._id = urlparse(self.url).path.strip('/').split('/')[1]
            return

        raise ValueError(f'Unsupported Youtube url type: {self._url_type}')


    @classmethod
    def from_id(
        cls,
        id: str
    ) -> 'YoutubePostUrl':
        """
        Get the `YoutubePostUrl` instance that
        includes the `id` provided, if
        valid.
        """
        if not YoutubePostUrlRegularExpression.YOUTUBE_POST_ID_REGEX.is_valid(id):
            raise ValueError(f'Invalid YouTube video id: {id}')

        url = f'https://www.youtube.com/watch?v={id}'

        return cls(
            url = url
        )


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
            print(e)
            return False

        return True
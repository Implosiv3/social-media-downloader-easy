from social_media_downloader_easy.platform.youtube.regex import YoutubeVideoUrlkRegularExpression
from social_media_downloader_easy.platform.youtube.enums import YoutubeUrlType
from dataclasses import dataclass
from urllib.parse import parse_qs, urlparse
from typing import Union

import re


@dataclass(frozen = True)
class YoutubeVideoUrl:
    """
    Class to handle a Youtube video url and
    also parse or validate them.
    """

    video_id: str
    url_type: YoutubeUrlType
    """
    The original url type this instance was
    built with.
    """

    @property
    def watch_url(
        self
    ) -> str:
        """
        The long format of the Youtube video.

        It is like this:
        - https://www.youtube.com/watch?v={self.video_id}
        """
        return f'https://www.youtube.com/watch?v={self.video_id}'


    @property
    def v_url(
        self
    ) -> str:
        """
        Another format with the '/v/' in the
        middle.

        It is like this:
        - https://www.youtube.com/v/{self.video_id}
        """
        return f'https://www.youtube.com/v/{self.video_id}'
    

    @property
    def short_url(
        self
    ) -> str:
        """
        The short format of the Youtube video.

        It is like this:
        - https://youtu.be/{self.video_id}
        """
        return f'https://youtu.be/{self.video_id}'


    @property
    def shorts_url(
        self
    ) -> str:
        """
        The url of the video for the shorts
        section.

        It is like this:
        - https://www.youtube.com/shorts/{self.video_id}
        """
        return f'https://www.youtube.com/shorts/{self.video_id}'


    @property
    def embed_url(
        self
    ) -> str:
        """
        The url to embed the Youtube video or
        short.

        It is like this:
        - `https://www.youtube.com/embed/{self.video_id}`
        """
        return f'https://www.youtube.com/embed/{self.video_id}'


    @property
    def thumbnail_url(
        self
    ) -> str:
        """
        The direct url to get the thumbnail.

        It is like this:
        - https://img.youtube.com/vi/{self.video_id}/oardefault.jpg
        """
        return f'https://img.youtube.com/vi/{self.video_id}/oardefault.jpg'


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
        if not YoutubeVideoUrlkRegularExpression.YOUTUBE_VIDEO_ID_REGEX.is_valid(video_id):
            raise ValueError(f'Invalid YouTube video ID: {video_id}')

        return cls(
            video_id = video_id,
            url_type = YoutubeUrlType.WATCH,
        )


    @classmethod
    def parse(
        cls,
        url: str
    ) -> Union['YoutubeVideoUrl', None]:
        """
        Parse the Youtube `url` provided and return
        a `YoutubeVideoUrl` instance if parseable.

        This method is accepting:
        - https://www.youtube.com/watch?v=dQw4w9WgXcQ
        - https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s
        - https://www.youtube.com/watch?feature=share&v=dQw4w9WgXcQ
        - https://youtu.be/dQw4w9WgXcQ
        - https://youtu.be/dQw4w9WgXcQ?t=30
        - https://www.youtube.com/shorts/dQw4w9WgXcQ
        - https://www.youtube.com/embed/dQw4w9WgXcQ
        - https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ
        - https://www.youtube.com/v/dQw4w9WgXcQ
        """
        parsed = urlparse(url)

        if parsed.scheme not in ('http', 'https'):
            return None

        hostname = parsed.hostname
        if hostname is None:
            return None

        hostname = hostname.lower()

        # youtu.be/VIDEO_ID
        if hostname == 'youtu.be':
            video_id = parsed.path.strip('/').split('/')[0]

            if YoutubeVideoUrlkRegularExpression.YOUTUBE_VIDEO_ID_REGEX.fullmatch(video_id, re.IGNORECASE):
                return cls(
                    video_id = video_id,
                    url_type = YoutubeUrlType.SHORT_URL,
                )

            return None

        # youtube.com / www.youtube.com / youtube-nocookie.com
        if hostname not in {
            'youtube.com',
            'www.youtube.com',
            'youtube-nocookie.com',
            'www.youtube-nocookie.com',
        }:
            return None

        path = parsed.path.rstrip('/')

        # /watch?v=VIDEO_ID
        if path == '/watch':
            video_id = parse_qs(parsed.query).get('v', [None])[0]

            if (
                video_id and
                YoutubeVideoUrlkRegularExpression.YOUTUBE_VIDEO_ID_REGEX.fullmatch(video_id, re.IGNORECASE)
            ):
                return cls(
                    video_id = video_id,
                    url_type = YoutubeUrlType.WATCH,
                )

            return None

        # /shorts/VIDEO_ID
        match = re.fullmatch(
            rf'/shorts/({YoutubeVideoUrlkRegularExpression.YOUTUBE_VIDEO_ID_REGEX.value})',
            path,
            re.IGNORECASE
        )

        if match:
            return cls(
                video_id = match.group(1),
                url_type = YoutubeUrlType.SHORTS,
            )

        # /embed/VIDEO_ID
        match = re.fullmatch(
            rf'/embed/({YoutubeVideoUrlkRegularExpression.YOUTUBE_VIDEO_ID_REGEX.value})',
            path,
            re.IGNORECASE
        )

        if match:
            return cls(
                video_id = match.group(1),
                url_type = YoutubeUrlType.EMBED,
            )

        # /v/VIDEO_ID
        match = re.fullmatch(
            rf'/v/({YoutubeVideoUrlkRegularExpression.YOUTUBE_VIDEO_ID_REGEX.value})',
            path,
            re.IGNORECASE
        )

        if match:
            return cls(
                video_id = match.group(1),
                url_type = YoutubeUrlType.V,
            )

        return None


    @classmethod
    def is_valid(
        cls,
        url: str
    ) -> bool:
        """
        Check if the `url` provided is valid Youtube
        video url or not.
        """
        return cls.parse(url) is not None
from social_media_downloader.downloader.facebook.consts import SERVERLESS_TOOLY_GATEWAY_DOWNLOAD_FACEBOOK_VIDEO_ENDPOINT_URL, SERVERLESS_TOOLY_GATEWAY_HEADERS
from social_media_downloader.downloader.facebook.regex import FacebookVideoLinkRegularExpression
from file_easy.dataclasses.file_resource import FileResource

import re


class _FacebookDownloader:
    """
    *For internal use only*

    Shortcut to the functionality related to
    Facebook.
    """

    def __init__(
        self,
        social_media_downloader: 'SocialMediaDownloader'
    ):
        self._social_media_downloader: 'SocialMediaDownloader' = social_media_downloader
        """
        *For internal use only*

        The reference to the `SocialMediaDownloader` parent.
        """

    async def get_download_url(
        self,
        # TODO: Accept IDs also
        url: str,
        output_filename: str
    ) -> FileResource:
        """
        Download the Facebook video from the given `url`
        and save it locally with the `output_filename`
        file name provided.

        The `url` must be like one of these:
        - https://www.facebook.com/share/r/1L6vVe9TjZ/
        - https://www.facebook.com/reel/875491608967954/
        - https://www.facebook.com/facebook/videos/875491608967954/
        - https://www.facebook.com/watch/?v=875491608967954
        - https://www.facebook.com/RolandGarros/videos/FOO/10155404760334920
        - https://www.facebook.com/RolandGarros/videos/10155404760334920/FOO
        
        This method will call an specific endpoint to
        obtain the result.
        """
        if not FacebookVideoLinkRegularExpression.is_valid_url(url):
            raise Exception(f'The "url" provided is not a valid Facebook url: {url}')

        # Valid for this method
        VALID_URL_REGEX = [
            FacebookVideoLinkRegularExpression.FACEBOOK_SHARED_REEL_REGEX.value,
            FacebookVideoLinkRegularExpression.FACEBOOK_REEL_REGEX.value,
            FacebookVideoLinkRegularExpression.FACEBOOK_VIDEO_REGEX.value,
            FacebookVideoLinkRegularExpression.FACEBOOK_WATCH_REGEX.value,
            FacebookVideoLinkRegularExpression.FACEBOOK_VIDEOS_SUFFIX_REGEX.value,
            FacebookVideoLinkRegularExpression.FACEBOOK_VIDEOS_PREFIX_REGEX.value
        ]

        if not any(re.fullmatch(regex, url) for regex in VALID_URL_REGEX):
            raise ValueError(f'URL not accepted for this way of downloading: {url}')
        
        params = {
            'url': url,
        }

        with self._social_media_downloader._file_downloader.follow_redirects(True):
            async with await self._social_media_downloader._file_downloader.client.get.stream(
                url = SERVERLESS_TOOLY_GATEWAY_DOWNLOAD_FACEBOOK_VIDEO_ENDPOINT_URL,
                headers = SERVERLESS_TOOLY_GATEWAY_HEADERS,
                params = params
            ) as response:
                await response.aread()
                json_response = response.json()
                video_url = json_response['videos']['hd']['url']

                return video_url

                #  TODO: This is to download
                file_resource = await self._social_media_downloader._file_downloader._get_file(
                    url = video_url,
                    output_filename = output_filename
                    # TODO: Allow it when 'Output' is public
                    # output_filename = Output.get_filename(
                    #     filename = output_filename,
                    #     file_extension = VideoFileExtension
                    # )
                )

                file_resource.source_url = video_url

                return file_resource 
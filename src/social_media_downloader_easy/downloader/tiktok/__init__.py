from social_media_downloader_easy.downloader.tiktok.consts import TIKWM_API_HEADERS, TIKWM_API_URL
from social_media_downloader_easy.downloader.tiktok.dataclasses import TikTokVideo
from social_media_downloader_easy.downloader.tiktok.regex import TiktokVideoLinkRegularExpression
from social_media_downloader_easy.downloader.tiktok.url_parser import TiktokUrlParser
from social_media_downloader_easy.platform.tiktok.dataclasses import TiktokPostUrl

import re



class _TiktokDownloader:
    """
    *For internal use only*

    Shortcut to the functionality related to
    Tiktok.
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

    
    async def get_download_url_new(
        self,
        url: str
    ) -> str:
        """
        Get the url to download the video from
        Tiktok with the `url` given.
        """
        url = TiktokPostUrl(url).long_url

        params = {
            'url': url,
            'hd': '1',
        }

        with self._social_media_downloader._file_downloader.follow_redirects(True):
            async with await self._social_media_downloader._file_downloader.client.get.stream(
                url = TIKWM_API_URL,
                headers = TIKWM_API_HEADERS,
                params = params
            ) as response:
                await response.aread()
                json_response = response.json()
                tiktok_video = TikTokVideo.from_dict(json_response.get('data'))

                return tiktok_video.url_without_watermark



    """
    TODO: This must be removed if the new method
    is working, because the new one is accepting
    and managing the urls properly, and this old
    method is limited and raising exceptions when
    it shouldn't.
    """
    async def get_download_url(
        self,
        # TODO: Accept IDs also
        url: str,
    ) -> str:
        """
        Download the Tiktok video from the given `url`
        and save it locally with the `output_filename`
        file name provided.

        The `url` must be like one of these:
        - https://www.tiktok.com/@numloco1/video/7632085075613502734
        - https://vm.tiktok.com/ZN8eRVqJa
        """
        if not TiktokVideoLinkRegularExpression.is_valid_url(url):
            raise Exception(f'The "url" provided is not a valid Tiktok url: {url}')

        # Valid for this method
        VALID_URL_REGEX = [
            TiktokVideoLinkRegularExpression.TIKTOK_VIDEO_LONG_REGEX.value,
            TiktokVideoLinkRegularExpression.TIKTOK_VIDEO_SHORT_REGEX.value
        ]

        if not any(re.fullmatch(regex, url) for regex in VALID_URL_REGEX):
            raise ValueError(f'URL not accepted for this way of downloading: {url}')

        with self._social_media_downloader._file_downloader.follow_redirects(True):
            tiktok_video_info = await TiktokUrlParser.parse(url)

            # We force it to be large url
            params = {
                'url': tiktok_video_info.url,
                'hd': '1',
            }

            async with await self._social_media_downloader._file_downloader.client.get.stream(
                url = TIKWM_API_URL,
                headers = TIKWM_API_HEADERS,
                params = params
            ) as response:
                await response.aread()
                json_response = response.json()
                tiktok_video = TikTokVideo.from_dict(json_response.get('data'))

                return tiktok_video.url_without_watermark
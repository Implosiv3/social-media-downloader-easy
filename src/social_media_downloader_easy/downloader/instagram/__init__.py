from social_media_downloader_easy.downloader.instagram.consts import IGMEDIA_DOWNLOAD_INSTAGRAM_VIDEO_HMAC_SECRET, IGMEDIA_DOWNLOAD_INSTAGRAM_VIDEO_ENDPOINT_URL
from social_media_downloader_easy.downloader.instagram.regex import InstagramVideoLinkRegularExpression
from social_media_downloader_easy.platform.instagram.dataclasses import InstagramPostUrl

import time
import json
import uuid
import hmac
import hashlib
import re


class _InstagramDownloader:
    """
    *For internal use only*

    Shortcut to the functionality related to
    Instagram.
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
        Instagram with the `url` given.
        """
        url = InstagramPostUrl(url).reel_url

        headers, body = _get_request_headers_and_body(url)

        with self._social_media_downloader._file_downloader.follow_redirects(True):
            async with await self._social_media_downloader._file_downloader.client.post.stream(
                url = IGMEDIA_DOWNLOAD_INSTAGRAM_VIDEO_ENDPOINT_URL,
                headers = headers,
                content = body
            ) as response:
                await response.aread()
                json_response = response.json()
                video_url = json_response['elements'][0]['url']

                return video_url


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
        url: str
    ) -> str:
        """
        Download the Facebook video from the given `url`
        and save it locally with the `output_filename`
        file name provided.

        The `url` must be like this:
        - https://www.instagram.com/reel/DHQf6RmMFtf/?igsh=ZBDzeTA4cWkwbW4w

        The urls below are not working for this method.
        - https://www.instagram.com/share/DHtsmGHTOn4
        - https://www.instagram.com/reels/DHtsmGHTOn4/
        - https://www.instagram.com/p/DHtsmGHTOn4/
        
        This method will call an specific endpoint to
        obtain the result.
        """
        if not InstagramVideoLinkRegularExpression.is_valid_url(url):
            raise Exception(f'The "url" provided is not a valid Instagram url: {url}')

        # Valid for this method
        VALID_URL_REGEX = [
            InstagramVideoLinkRegularExpression.INSTAGRAM_REEL_REGEX.value,
            InstagramVideoLinkRegularExpression.INSTAGRAM_POST_REGEX.value
        ]

        if not any(re.fullmatch(regex, url) for regex in VALID_URL_REGEX):
            raise ValueError(f'URL not accepted for this way of downloading: {url}')

        headers, body = _get_request_headers_and_body(url)

        with self._social_media_downloader._file_downloader.follow_redirects(True):
            async with await self._social_media_downloader._file_downloader.client.post.stream(
                url = IGMEDIA_DOWNLOAD_INSTAGRAM_VIDEO_ENDPOINT_URL,
                headers = headers,
                content = body
            ) as response:
                await response.aread()
                json_response = response.json()
                video_url = json_response['elements'][0]['url']

                return video_url


"""
The way this request is made was found in this file:
- https://www.ig.media/assets/chunks/chunk-D_lA2Uui.js

And we've found the code needed to replicate a valid
request directly.
"""

def _get_request_headers_and_body(
    url: str
) -> tuple[dict, dict]:
    """
    Get the headers and the body to make a request
    and download a video from Instagram.

    They will be returned as a tuple:
    - `(headers, body)`
    """
    # 1st. Get the body
    payload = {
        'url': url,
        # A valid sessionId I had in the past:
        # 'ab44d080-fbc8-4466-b035-4c1a6abbe608'
        'sessionId': str(uuid.uuid4()),
        'version': '0.1.58'
    }

    # The body has to be the exact json
    body = json.dumps(payload, separators = (',', ':'))

    # 2nd. Get the headers by using the body
    # Timestamp in ms as str
    # In javascript: 'x-timestamp' = Date.now().toString()
    timestamp = str(int(time.time() * 1000))
    # Signed str
    message = f'{timestamp}.{body}'

    # HMAC SHA256 HEX
    # In javascript: 'x-hmac-signature': nx.HmacSHA256(d, this.HMAC_SECRET).toString(nx.enc.Hex)
    signature = hmac.new(
        IGMEDIA_DOWNLOAD_INSTAGRAM_VIDEO_HMAC_SECRET.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    headers = {
        'Content-Type': 'application/json',
        # A value that was valid in the past:
        # 'x-hmac-signature': '6d4fd85af287b6d389ac1ece7dfa4c9b45d760fa6c2b5dabf0b4076ff6a6d9bb',
        'x-hmac-signature': signature,
        # A value that was valid in the past:
        # 'x-timestamp': '1779082613645',
        'x-timestamp': timestamp,
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://www.ig.media/',
        'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
    }

    return headers, body

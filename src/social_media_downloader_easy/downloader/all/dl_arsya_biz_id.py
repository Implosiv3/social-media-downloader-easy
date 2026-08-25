"""
Based on this platform:
- https://dl.arsya.biz.id/

That uses this API endpoint:
- https://dl.arsya.biz.id/api/download?url=[URL]

Example of a valid endpoint url:
- https://dl.arsya.biz.id/api/download?url=https%3A%2F%2Fwww.instagram.com%2Freel%2FDHtsmGHTOn4%2F&deviceType=desktop
"""
from httpx_easy import HttpClient


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json,text/plain,*/*",
    "Accept-Language": "es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://dl.arsya.biz.id/",
    "Origin": "https://dl.arsya.biz.id",
}


class _DlArsyaBizIdDownloader:
    """
    *For internal use only*

    Class to include the functionality of a
    universal video downloader app.
    """

    async def get_download_url(
        self,
        video_url: str
    ):
        # TODO: Validate the 'video_url'
        endpoint_url = f'https://dl.arsya.biz.id/api/download?url={video_url}&deviceType=desktop'

        with HttpClient(default_headers = HEADERS) as http_client:
            response = http_client.get.complete(
                url = endpoint_url
            )

            data = response.json()
            media = data['data']['media'][0]

            # thumbnail_url = media['thumbnail']
            video_url = media['url']

            return video_url
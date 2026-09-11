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

        """
        TODO: If you navigate to that endpoint
        with the scraper, it will give you the
        whole json as the answer, the content
        displayed on the page.
        """

        with HttpClient(default_headers = HEADERS) as http_client:
            response = http_client.get.complete(
                url = endpoint_url
            )

            data = response.json()
            media = data['data']['media'][0]

            # thumbnail_url = media['thumbnail']
            video_url = media['url']

            return video_url


"""
Example of a response:

{
    "creator":"@arsya - github.com/arsya371",
    "status":true,
    "data":{
        "media":[
            {
                "thumbnail":"https://d.rapidcdn.app/thumb?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJodHRwczovL3Njb250ZW50LWFtczItMS5jZG5pbnN0YWdyYW0uY29tL3YvdDUxLjcxODc4LTE1LzQ4NjQyMjcxNl8zMDM4MTUxOTE2MzM2Mjg1XzQxMzM0ODYyMjAxNzQwMDY1MjRfbi5qcGc_c3RwPWRzdC1qcGdfZTE1X3R0NiZfbmNfY2F0PTEwNSZpZ19jYWNoZV9rZXk9TXpVNU56Y3lOemd3T1RJNU1EUXpNRGsyT0ElM0QlM0QuMy1jY2I3LTUmY2NiPTctNSZfbmNfc2lkPTU4Y2RhZCZlZmc9ZXlKMlpXNWpiMlJsWDNSaFp5STZJa05NU1ZCVExuaHdhV1J6TGpZME1DNXpaSEl1ZG1sa1pXOWZaR1ZtWVhWc2RGOWpiM1psY2w5bWNtRnRaUzVETXlKOSZfbmNfb2hjPXhLbUVJUmExQ21rUTdrTnZ3RnJUSVZHJl9uY19vYz1BZHBicjRwOHhMYlBkMU1FMUo0alZRakRvWmR2QmEzQmZ0M2hnNzducVVqQ2xSX0ZELURra19wbUpmRWlxWmhIaFBRJl9uY19hZD16LW0mX25jX2NpZD0wJl9uY196dD0yMyZfbmNfaHQ9c2NvbnRlbnQtYW1zMi0xLmNkbmluc3RhZ3JhbS5jb20mX25jX2dpZD0zYTJYYURQckM5T21kTjZ5U05lRDZnJl9uY19zcz03YTIyZSZvaD0wMF9BUUlFZnJ1STV6NFkyaUJtaW5GdkgxZ0dzWllSRzA1LWRVWHotLWpPQ3NtcDFBJm9lPTZBQTk5QUJEIiwiaGVhZGVycyI6eyJ1c2VyLWFnZW50IjoiVGVsZWdyYW1Cb3QgKGxpa2UgVHdpdHRlckJvdCkifSwiaWF0IjoxNzg5MTIzNTQzfQ.zHuGSFbc8yqWVP6XWfcLHjjJNkJb5qj6yEs1pRrXNQE",
                "url":"https://d.rapidcdn.app/v2?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJodHRwczovL3Njb250ZW50LWFtczItMS5jZG5pbnN0YWdyYW0uY29tL28xL3YvdDIvZjIvbTM2Ny9BUU9oZFdHR1pSVWdvaUVDN1E4WlFpLWRNSUNVNThIZnVZZUlQSU9wNDIxSXRMYk1sTVdTZThqRGVndDB2ZnNicnlYUUhUT2dnOGZCQ21LbFNiVTFpWFE1YkZUTmhBa0NuX0ZfZFlFLm1wND9fbmNfY2F0PTExMCZfbmNfc2lkPTVlOTg1MSZfbmNfaHQ9c2NvbnRlbnQtYW1zMi0xLmNkbmluc3RhZ3JhbS5jb20mX25jX29oYz1SQUdhQkU3N19XSVE3a052d0ZJcFd4dCZlZmc9ZXlKMlpXNWpiMlJsWDNSaFp5STZJbmh3ZGw5d2NtOW5jbVZ6YzJsMlpTNUpUbE5VUVVkU1FVMHVRMHhKVUZNdVF6TXVOekl3TG1SaGMyaGZZbUZ6Wld4cGJtVmZNVjkyTVNJc0luaHdkbDloYzNObGRGOXBaQ0k2TXpVME56a3hNVGt6TWpFNE1UTTFOQ3dpWVhOelpYUmZZV2RsWDJSaGVYTWlPalV6TWl3aWRtbGZkWE5sWTJGelpWOXBaQ0k2TVRBd09Ua3NJbVIxY21GMGFXOXVYM01pT2pJMUxDSjFjbXhuWlc1ZmMyOTFjbU5sSWpvaWQzZDNJbjAlM0QmY2NiPTE3LTEmdnM9NjhkOTU3YzA0Y2Q3ZGQ0MCZfbmNfdnM9SEJrc0ZRSVlRR2xuWDJWd2FHVnRaWEpoYkM4MVF6UXpOVGt3TXpZMk56TXdNa016TXpCR01qY3pRMFEzUVVJeE0wRTROVjkyYVdSbGIxOWtZWE5vYVc1cGRDNXRjRFFWQUFMSUFSSUFGUUlZUjJsblgzaHdkbDl5WldWc2MxOXdaWEp0WVc1bGJuUmZjM0pmY0hKdlpDOHhOVGd5TmpVd05EWXlORFV4TXpVMVh6VTBNVGs0TURRNU5Ea3pPVFkyT1RNMU56UXViWEEwRlFJQ3lBRVNBQ2dBR0FBYkFvZ0hkWE5sWDI5cGJBRXhFbkJ5YjJkeVpYTnphWFpsWDNKbFkybHdaUUV4RlFBQUp0VHR5LWJUczgwTUZRSW9Ba016TEJkQU9UdWw0MVAzenhnU1pHRnphRjlpWVhObGJHbHVaVjh4WDNZeEVRQjFfZ2RsNXAwQkFBJl9uY19naWQ9M2EyWGFEUHJDOU9tZE42eVNOZUQ2ZyZfbmNfenQ9MjgmX25jX3NzPTdhMjJlJm9oPTAwX0FRSm9nV1NMY2w2MXFGcUdVMHU1bU5GUWtqNHpjOGpBUjNldHhsVnAzYmc1MFEmb2U9NkFBOUM5NEIiLCJmaWxlbmFtZSI6InNuYXBzYXZlLWFwcF8zNTk3NzI3ODA5MjkwNDMwOTY4XzU4MzY3ODgxMzIubXA0IiwiaGVhZGVycyI6eyJ1c2VyLWFnZW50IjoiVGVsZWdyYW1Cb3QgKGxpa2UgVHdpdHRlckJvdCkifSwiaWF0IjoxNzg5MTIzNTQzfQ.rxu7FOu1lyVisCXgVUq4XPU0qR3MDJlCAn7FEcl_t44&dl=1&dl=1"
            }
        ]
    }
}
"""
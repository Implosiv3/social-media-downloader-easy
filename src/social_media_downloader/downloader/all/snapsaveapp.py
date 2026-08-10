"""
TODO: This module is being tested and it
is experimental by now.

I found this project on Github:
- https://github.com/arsya371

That has a public website:
- https://dl.arsya.biz.id/

In that website you paste the video url
and, waiting a bit, get the thumbnail and
the url to download, directly.

It is based on the Snapsave platform:
- https://snapsave.app/download-video-instagram

This platform has different sections to
download from the different platforms, but
there is always a call to this endpoint
(https://snapsave.app/action.php?lang=en)
that includes the `url` as `From Data`
(https://www.instagram.com/reel/DHtsmGHTOn4/
for example).

After a few seconds, there is a response 
that is ofuscated javascript, that I was
able to collect (see code at the bottom of
this file). There you have the direct url
to download the video.

So, basically, the project I said before
making a request to this endpoint and
redirecting the response to us, thats all.

We can ask to that project, but if it is
desactivated, we lost the functionality.
Thats why we should try to request to the
Snappsave endpoint directly and redirect
the link by ourselves.
"""
from web_scraper_easy.chrome import ChromeScraper
from web_scraper_easy.chrome.dataclasses.options_argument import StartMaximizedChromeOptionsArgument

import re
import httpx


# TODO: Maybe use scraper headers (?)
HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7",
    "Origin": "https://snapsave.app",
    "Referer": "https://snapsave.app/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    ),
}
SNAPSAVE_URL = "https://snapsave.app/action.php"
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/"


class _SnapsaveDownloader:
    """
    *For internal use only*
    
    Class to download videos by using the
    Snapsave platform and its specific
    endpoint.
    """

    # TODO: By now is giving the url
    def download(
        self,
        video_url: str
    ):
        """
        Download the video with the `video_url` given.

        This method will perform a httpx request to
        the Snapsave endpoint to obtain ofuscated
        javascript code that will be decoded and
        transformed into the direct download link
        for the video.

        It will launch a chrome scraper to obtain
        valid cookies in order to make the request
        that gives us the url to download the file.
        """
        chrome_scraper = ChromeScraper.init(
            # We need GUI to get cookies
            do_use_gui = True,
            additional_options = [
                StartMaximizedChromeOptionsArgument
            ]
        )

        chrome_scraper.go_to_web_and_wait_until_loaded('https://snapsave.app/')

        """
        TODO: This could fail if something from
        Cloudflare appears while navigating and
        we don't wait until it is completed to
        obtain the cookie.
        """
        with httpx.Client(
            headers = HEADERS,
            cookies = chrome_scraper.cookies,
            timeout = 90.0,
            follow_redirects = True,
        ) as client:
            response = client.post(
                SNAPSAVE_URL,
                params = {'lang': 'en'},
                files = {
                    'url': (None, video_url),
                },
            )

            response.raise_for_status()

            decoded = _decode_snapsave_response(response.text)

        # We could remove this line below...
        chrome_scraper.wait(1)

        download_url = _extract_download_url(decoded)

        return download_url

        # with self._social_media_downloader._file_downloader.follow_redirects(True):
        #     async with await self._social_media_downloader._file_downloader.client.get.stream(
        #         url = SERVERLESS_TOOLY_GATEWAY_DOWNLOAD_FACEBOOK_VIDEO_ENDPOINT_URL,
        #         headers = SERVERLESS_TOOLY_GATEWAY_HEADERS,
        #         params = params
        #     ) as response:
        #         await response.aread()
        #         json_response = response.json()
        #         video_url = json_response['videos']['hd']['url']

        #         file_resource = await self._social_media_downloader._file_downloader._get_file(
        #             url = video_url,
        #             output_filename = output_filename
        #             # TODO: Allow it when 'Output' is public
        #             # output_filename = Output.get_filename(
        #             #     filename = output_filename,
        #             #     file_extension = VideoFileExtension
        #             # )
        #         )

        #         file_resource.source_url = video_url

        #         return file_resource 

        return download_url



def _decode_snapsave_response(
    text: str
) -> str:
    """
    *For internal use only*

    The response is ofuscated code and must
    be decoded. You can see a decoded example
    at the bottom of this file.
    """
    pattern = re.compile(
        r'eval\(function\(h,u,n,t,e,r\).*?'
        r'\}\(\s*'
        r'"(?P<data>.*?)"\s*,\s*'
        r'(?P<u>\d+)\s*,\s*'
        r'"(?P<n>[^"]+)"\s*,\s*'
        r'(?P<t>\d+)\s*,\s*'
        r'(?P<e>\d+)\s*,\s*'
        r'(?P<r>\d+)'
        r'\)\)',
        re.DOTALL,
    )

    match = pattern.search(text)

    if not match:
        raise RuntimeError('The parameters of the ofuscated code were not found.')

    data = match.group('data')
    u = int(match.group('u'))
    n = match.group('n')
    t = int(match.group('t'))
    e = int(match.group('e'))
    r = int(match.group('r'))

    if e >= len(n):
        raise RuntimeError(
            f"Invalid parameter: e={e}, but n={n!r} "
            f"It only has {len(n)} characters."
        )

    delimiter = n[e]

    source_alphabet = ALPHABET[:e]
    output_alphabet = ALPHABET[:10]

    def decode_value(
        value: str
    ) -> int:
        """
        Decode the `value` provided.

        Equivalent to _0xe73c(d, e, 10).
        """
        value = value[::-1]

        result = 0

        for position, char in enumerate(value):
            index = source_alphabet.find(char)

            if index != -1:
                result += index * (e ** position)

        return result

    decoded = []
    index = 0
    while index < len(data):
        value = ''

        while index < len(data) and data[index] != delimiter:
            value += data[index]
            index += 1

        for j, char in enumerate(n):
            value = value.replace(char, str(j))

        number = decode_value(value)
        decoded.append(chr(number - t))

        index += 1

    return ''.join(decoded)


def _extract_download_url(
    decoded: str
) -> str:
    """
    *For internal use only*

    Extract the url to download the video from
    the decodified html code received from the
    Snapsave app endpoint.
    """
    match = re.search(
        r'https://d\.rapidcdn\.app/v2\?[^"\s\\)<>]+',
        decoded,
    )

    if not match:
        raise RuntimeError(
            "No se encontró la URL de descarga.\n\n"
            f"Respuesta decodificada:\n{decoded[:5000]}"
        )

    return match.group(0)



"""
Code intercepted:

=== CÓDIGO DESOFUSCADO ===
VM5352:5 if((Math.round(+new Date()/1000)) < 1786365662){if(window.location.hostname==='dev.snapsave.app' || window.location.hostname==='snapsave.app' ){document.getElementById("download-section").innerHTML = "<style>.download-box img{width:100%;height:100%;top:0;left:0;right:0;bottom:0;object-fit:cover}.format-icon{position:absolute;z-index:10;top:8px;right:8px}i.icon{display:table-cell;height:2em;width:2em}.icon-dlimage{background:url(/img/iconimage.svg) no-repeat center}.icon-dlvideo{background:url(/img/iconvideo.svg) no-repeat center}.download-items__btn a{display:block}.download-items{position:relative}.download-items__btn{position:absolute;width:calc(100% - 32px);bottom:1rem;left:1rem;right:0}.row{--bs-gutter-x:1.5rem;--bs-gutter-y:0;display:flex;flex-wrap:wrap;margin-top:calc(var(--bs-gutter-y) * -1);margin-right:calc(var(--bs-gutter-x) * -.5);margin-left:calc(var(--bs-gutter-x) * -.5)}.row>*{flex-shrink:0;width:100%;max-width:100%;padding-right:calc(var(--bs-gutter-x) * .5);padding-left:calc(var(--bs-gutter-x) * .5);margin-top:var(--bs-gutter-y)}@media (min-width:576px){.col-sm-4{flex:0 0 auto;width:33.33333333%}}</style><section class=\"section\"><div class=\"container download-box\"><div class=\"row\"><div class=\"col-sm-4\"><div class=\"download-items\"><div class=\"download-items__thumb\"><img src=\"https://d.rapidcdn.app/thumb?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJodHRwczovL3Njb250ZW50LWFtczItMS5jZG5pbnN0YWdyYW0uY29tL3YvdDUxLjcxODc4LTE1LzQ4NjQyMjcxNl8zMDM4MTUxOTE2MzM2Mjg1XzQxMzM0ODYyMjAxNzQwMDY1MjRfbi5qcGc_c3RwPWRzdC1qcGdfZTE1X3R0NiZfbmNfY2F0PTEwNSZpZ19jYWNoZV9rZXk9TXpVNU56Y3lOemd3T1RJNU1EUXpNRGsyT0ElM0QlM0QuMy1jY2I3LTUmY2NiPTctNSZfbmNfc2lkPTU4Y2RhZCZlZmc9ZXlKMlpXNWpiMlJsWDNSaFp5STZJa05NU1ZCVExuaHdhV1J6TGpZME1DNXpaSEl1ZG1sa1pXOWZaR1ZtWVhWc2RGOWpiM1psY2w5bWNtRnRaUzVETXlKOSZfbmNfb2hjPVNGNm13SnVwLU5NUTdrTnZ3SEpNdHhzJl9uY19vYz1BZG9JeFZMRWcxMHRNbmpPb2ZkUVV1bXFBaHBxT0xnazhWamk2bGx4dnI1aThzNnlONHYzUm9OMkotVzVUWTlkaXJnJl9uY19hZD16LW0mX25jX2NpZD0wJl9uY196dD0yMyZfbmNfaHQ9c2NvbnRlbnQtYW1zMi0xLmNkbmluc3RhZ3JhbS5jb20mX25jX2dpZD1pSTdLRVdIa3JUZmFycU9ncjVvVVRRJl9uY19zcz03YTIyZSZvaD0wMF9BUUV3RXh5R1dJUjZxbFBEc1cwNUN3OXl3N184cEMxUXRKdm41MTVhN0hLdVBnJm9lPTZBN0Y2QUJEIiwiaGVhZGVycyI6eyJ1c2VyLWFnZW50IjoiVGVsZWdyYW1Cb3QgKGxpa2UgVHdpdHRlckJvdCkifSwiaWF0IjoxNzg2MzYyMDYyfQ.a88lT-lDZGA5yFVA7VHtJAbE2iV3jGrYwTOBC61jHzc\" alt=\"Download Instagram SnapX\"><span class=\"format-icon\"><i class=\"icon icon-dlvideo\"></i></span></div><div class=\"download-items__btn\"><a onclick=\"showAd();\" href=\"https://d.rapidcdn.app/v2?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJodHRwczovL3Njb250ZW50LWFtczItMS5jZG5pbnN0YWdyYW0uY29tL28xL3YvdDIvZjIvbTM2Ny9BUU9oZFdHR1pSVWdvaUVDN1E4WlFpLWRNSUNVNThIZnVZZUlQSU9wNDIxSXRMYk1sTVdTZThqRGVndDB2ZnNicnlYUUhUT2dnOGZCQ21LbFNiVTFpWFE1YkZUTmhBa0NuX0ZfZFlFLm1wND9fbmNfY2F0PTExMCZfbmNfc2lkPTVlOTg1MSZfbmNfaHQ9c2NvbnRlbnQtYW1zMi0xLmNkbmluc3RhZ3JhbS5jb20mX25jX29oYz1rN2tTYjEtcVZRd1E3a052d0dlckswSCZlZmc9ZXlKMlpXNWpiMlJsWDNSaFp5STZJbmh3ZGw5d2NtOW5jbVZ6YzJsMlpTNUpUbE5VUVVkU1FVMHVRMHhKVUZNdVF6TXVOekl3TG1SaGMyaGZZbUZ6Wld4cGJtVmZNVjkyTVNJc0luaHdkbDloYzNObGRGOXBaQ0k2TXpVME56a3hNVGt6TWpFNE1UTTFOQ3dpWVhOelpYUmZZV2RsWDJSaGVYTWlPalV3TUN3aWRtbGZkWE5sWTJGelpWOXBaQ0k2TVRBd09Ua3NJbVIxY21GMGFXOXVYM01pT2pJMUxDSjFjbXhuWlc1ZmMyOTFjbU5sSWpvaWQzZDNJbjAlM0QmY2NiPTE3LTEmdnM9NjhkOTU3YzA0Y2Q3ZGQ0MCZfbmNfdnM9SEJrc0ZRSVlRR2xuWDJWd2FHVnRaWEpoYkM4MVF6UXpOVGt3TXpZMk56TXdNa016TXpCR01qY3pRMFEzUVVJeE0wRTROVjkyYVdSbGIxOWtZWE5vYVc1cGRDNXRjRFFWQUFMSUFSSUFGUUlZUjJsblgzaHdkbDl5WldWc2MxOXdaWEp0WVc1bGJuUmZjM0pmY0hKdlpDOHhOVGd5TmpVd05EWXlORFV4TXpVMVh6VTBNVGs0TURRNU5Ea3pPVFkyT1RNMU56UXViWEEwRlFJQ3lBRVNBQ2dBR0FBYkFvZ0hkWE5sWDI5cGJBRXhFbkJ5YjJkeVpYTnphWFpsWDNKbFkybHdaUUV4RlFBQUp0VHR5LWJUczgwTUZRSW9Ba016TEJkQU9UdWw0MVAzenhnU1pHRnphRjlpWVhObGJHbHVaVjh4WDNZeEVRQjFfZ2RsNXAwQkFBJl9uY19naWQ9aUk3S0VXSGtyVGZhcnFPZ3I1b1VUUSZfbmNfenQ9MjgmX25jX3NzPTdhMjJlJm9oPTAwX0FRR25aV29TcmhmTDdXaks4V09wb0hFQ3FvVDNWT2pDbVN6aGloRmlWWjdCNHcmb2U9NkE3Rjk5NEIiLCJmaWxlbmFtZSI6InNuYXBzYXZlLWFwcF8zNTk3NzI3ODA5MjkwNDMwOTY4XzU4MzY3ODgxMzIubXA0IiwiaGVhZGVycyI6eyJ1c2VyLWFnZW50IjoiVGVsZWdyYW1Cb3QgKGxpa2UgVHdpdHRlckJvdCkifSwiaWF0IjoxNzg2MzYyMDYyfQ.K_qgFxKcA8D77NpqJmtoFzi7Q6JmHT-2-BPVmh6JvLU&dl=1&dl=1\" class=\"button is-success is-small mt-3\" rel=\"nofollow\" title=\"Download Photo\"><span>Download video</span></span></a></div></div></div><div class=\"col\"><a class=\"button is-dark is-small is-fullwidth\" href=\"/\" style=\"margin-top: 1rem\">Download more videos</a><a class=\"button is-dark is-small is-fullwidth\" target=\"_blank\" rel=\"nofollow noopener\" href=\"https://play.google.com/store/apps/details?id=com.snapd.video2026&referrer=web_organic\" style=\"margin-top: 1rem\">Download with app</a></div></div></div></section>"; document.getElementById("inputData").remove(); document.getElementById("why-section").remove(); document.getElementById("how-section").remove(); document.getElementById("faq-section").remove(); gtag("event", "get_video_success", { "cache_name": "1" });	var downloadLink = document.querySelector(".download-link");	let toElem = (getPosition(downloadLink).y / 2) + 80;	animate(document.scrollingElement || document.documentElement, "scrollTop", "", 0, toElem, 1500, true);}}
"""
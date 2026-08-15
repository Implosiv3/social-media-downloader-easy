from social_media_downloader_easy.platform.tiktok.regex import TiktokVideoUrlRegularExpression
from httpx_easy.client import HttpClient
from web_scraper_easy.chrome import ChromeScraper
from web_scraper_easy.chrome.dataclasses.options_argument import MuteAudioChromeOptionsArgument, CustomChromeOptionsArgument
from typing import Union

import re
import time


def short_tiktok_url_to_long_tiktok_url(
    url: str
) -> str:
    """
    Transform the short Tiktok `url` provided
    to its long format that includes the
    username and the real video id.
    """
    # TODO: Should we validate it here (?)
    # if not TiktokVideoUrlRegularExpression.TIKTOK_SHORT_URL_REGEX.is_valid(url):
    #     return None
    #     raise Exception('The "url" provided is not a short tiktok url.')
    
    with HttpClient(do_follow_redirects = True) as client:
        response = client.get.complete(
            url = url
        )
    
    return str(response.url)


def tiktok_video_id_to_long_tiktok_url(
    video_id: str
) -> str:
    """
    Obtain the long format url of the Tiktok
    video with the `video_id` provided.

    The `video_id` is only digits and its not
    the shortcode to share that comes in the
    short url.

    This method will navigate with a web
    scraper to get redirected and obtain the
    real url, and could need a captcha
    verification.
    """
    # TODO: Should we validate it here (?)
    # if not TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_ID_REGEX.is_valid(video_id):
    #     return None
    #     raise Exception('The "video_id" provided is not a valid Tiktok video id.')

    """
    There is no way to obtain the real url
    by the response obtained. It has to be
    a web navigator that waits until the
    page is redirected to the real one.
    """

    url = f'https://www.tiktok.com/@/video/{video_id}'
    # This one below redirects to the one on top
    # url = f'https://tiktok.com/share/video/{video_id}'

    # Use a common instance or something (?)
    chrome_scraper: ChromeScraper = ChromeScraper.init(
        do_use_gui = True,
        additional_options = [
            MuteAudioChromeOptionsArgument,
            # Disable auto-play
            CustomChromeOptionsArgument("--autoplay-policy=user-gesture-required"),
            CustomChromeOptionsArgument("--disable-audio-output")
            # "--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies"
        ]
    )

    chrome_scraper.go_to_web_and_wait_until_loaded(url)

    timeout = 10.0
    interval = 0.1
    start = time.monotonic()

    while time.monotonic() - start < timeout:
        current_url = chrome_scraper.current_url

        if current_url != url:
            return current_url

        time.sleep(interval)

    # TODO: What if not found (?)
    # return str(response.url)


def get_username_and_video_id_from_long_tiktok_url(
    url: str
) -> Union[tuple[str, str], None]:
    """
    Get the username and video id as a tuple
    from the Tiktok video long `url` provided.
    """
    # TODO: Should we validate it here (?)
    # if not TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_URL_REGEX.is_valid(url):
    #     return None
    #     raise Exception('The "url" provided is not a valid Tiktok url.')
    
    match = re.fullmatch(TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_URL_REGEX.value, url)

    return (
        match.group(1),
        match.group(2)
    )
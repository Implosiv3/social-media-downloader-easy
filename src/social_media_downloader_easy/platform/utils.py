from web_scraper_easy.chrome import ChromeScraper
from web_scraper_easy.chrome.dataclasses.options_argument import MuteAudioChromeOptionsArgument, CustomChromeOptionsArgument
from pystandards.regex import RegularExpression
from typing import Union

import time


def get_url_from_redirecting_url(
    url: str,
    regex: Union[RegularExpression, None],
    timeout: float = 10.0
) -> Union[str, None]:
    """
    Go to the `url` provided and wait until it
    is redirected to a new url that must match
    the `regex`, if provided, and that new url
    will be returned (or None if not redirected
    or not matching the `regex`).
    """
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

    interval = 0.1
    start = time.monotonic()

    while time.monotonic() - start < timeout:
        current_url = chrome_scraper.current_url

        if regex.is_valid(current_url):
            return current_url

        time.sleep(interval)

    return None
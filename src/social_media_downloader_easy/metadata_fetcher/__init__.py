from social_media_downloader_easy.metadata_fetcher.tiktok import _TiktokMetadataFetcher
from web_scraper_easy.chrome.dataclasses.options_argument import MuteAudioChromeOptionsArgument, CustomChromeOptionsArgument
from web_scraper_easy import ChromeScraper


class MetadataFetcher:
    """
    Class to fetch metadata from social media
    videos.
    """

    def __init__(
        self
    ):
        self._chrome_scraper: ChromeScraper = ChromeScraper.init(
            do_use_gui = False,
            additional_options = [
                MuteAudioChromeOptionsArgument,
                # Disable auto-play
                CustomChromeOptionsArgument("--autoplay-policy=user-gesture-required"),
                CustomChromeOptionsArgument("--disable-audio-output")
                # "--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies"
            ]
        )
        """
        *For internal use only*

        The chrome scraper instance that will perform the
        web navigation if needed.
        """

        self.tiktok: _TiktokMetadataFetcher = _TiktokMetadataFetcher(self)
        """
        Shortcut to the Tiktok metadata fetcher.
        """
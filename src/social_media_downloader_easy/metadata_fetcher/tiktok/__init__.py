from social_media_downloader_easy.downloader.tiktok.url_parser import TiktokUrlParser
from social_media_downloader_easy.downloader.tiktok.url_parser import _get_id_and_username_from_long_url
from social_media_downloader_easy.metadata_fetcher.tiktok.dataclasses import TiktokVideoMetadata, TikTokMetadataEmbed
from httpx_easy import HttpClient


class _TiktokMetadataFetcher:
    """
    Class to fetch metadata from the videos that
    are published in the Tiktok platform.
    """

    def __init__(
        self,
        metadata_fetcher: 'MetadataFetcher'
    ):
        self._metadata_fetcher: 'MetadataFetcher' = metadata_fetcher
        """
        *For internal use only*

        Reference to the `MetadataFetcher` parent
        instance that handles the web scraper to
        obtain some of the metadata we need.
        """


    def get_metadata(
        self,
        video_url: str
    ) -> TikTokMetadataEmbed:
        """
        Get the metadata of the Tiktok video with
        the `video_url` given.
        """
        # TODO: Validate tiktok url (can be short or long)
        endpoint_url = f'https://www.tiktok.com/oembed?url={video_url}'
        
        # Example of a valid endpoint url
        # https://www.tiktok.com/oembed?url=https://vm.tiktok.com/ZN8eRVqJa

        with HttpClient() as http_client:
            response = http_client.get.complete(endpoint_url)
            # with http_client.get.complete(endpoint_url) as response:
            return TikTokMetadataEmbed.from_dict(response.json())


    def get_metadata_with_chrome_scraper(
        self,
        video_url: str
    ) -> TiktokVideoMetadata:
        """
        Get the metadata of the Tiktok video with
        the `video_url` given.

        This is heavier and slower than the
        'get_metadata' method due to the web
        scraper that is needed.
        """
        self._validate_url(video_url)

        # TODO: The Chrome instance should be like this
        """
        chrome_scraper = ChromeScraper.init(
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
        self._metadata_fetcher._chrome_scraper.go_to_web_and_wait_until_loaded(video_url)
        
        description_element = self._metadata_fetcher._chrome_scraper.find_element_by_custom_tag_waiting(
            element_type = 'div',
            custom_tag = 'data-e2e',
            custom_tag_value = 'video-desc',
            time = 10
        )

        current_url = self._metadata_fetcher._chrome_scraper.current_url
        id, username = _get_id_and_username_from_long_url(current_url)

        description = self._metadata_fetcher._chrome_scraper.execute_script("""
            const root = arguments[0];
            let text = "";

            for (const node of root.childNodes) {

                if (node.nodeType === Node.TEXT_NODE) {
                    text += node.textContent;
                    continue;
                }

                if (node.nodeType !== Node.ELEMENT_NODE) {
                    continue;
                }

                if (node.tagName === "A") {
                    const hashtag = node.innerText.trim().replace(/^#/, "");
                    text += "#" + hashtag;
                } else {
                    text += node.innerText;
                }
            }

            return text.trim();
        """, description_element)

        title = self._metadata_fetcher._chrome_scraper.driver.title.replace(' | TikTok', '')

        return TiktokVideoMetadata(
            id = id,
            username = username,
            title = title,
            description = description
        )


    def _validate_url(
        self,
        url: str
    ):
        """
        *For internal use only*
        
        Validate the `url` provided and raise an
        exception if it is not valid.
        """
        if not TiktokUrlParser.is_valid(url):
            raise Exception(f'The provided "url" is not a valid Tiktok video url: {url}')
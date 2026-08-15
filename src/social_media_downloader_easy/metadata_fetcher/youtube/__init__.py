

class _YoutubeMetadataFetcher:
    """
    Class to fetch metadata from the videos that
    are published in the Youtube platform.
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


    async def get_thumbnail_url(
        self,
        video_url: str
    ) -> str:
        """
        Get the url of the thumbnail of the Youtube
        video with the `video_url` provided.
        """
        # TODO: We need the id of the youtube video url
        id = 'aRVd1QeyTiE'

        endpoint_url = f'https://img.youtube.com/vi/{id}/oardefault.jpg'

        # Example of a valid endpoint url
        # 'https://img.youtube.com/vi/aRVd1QeyTiE/oardefault.jpg'

        return endpoint_url

        # async with HttpClient() as http_client:
        #     async with await http_client.get.complete(endpoint_url) as response:
        #         return TikTokMetadataEmbed.from_dict(response.json())



    # def _validate_url(
    #     self,
    #     url: str
    # ):
    #     """
    #     *For internal use only*
        
    #     Validate the `url` provided and raise an
    #     exception if it is not valid.
    #     """
    #     if not YoutubeUrlParser.is_valid(url):
    #         raise Exception(f'The provided "url" is not a valid Youtube video url: {url}')
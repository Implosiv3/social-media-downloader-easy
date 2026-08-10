from social_media_downloader.downloader.facebook import _FacebookDownloader
from social_media_downloader.downloader.instagram import _InstagramDownloader
from social_media_downloader.downloader.tiktok import _TiktokDownloader
from social_media_downloader.downloader.all.snapsaveapp import _SnapsaveDownloader
from social_media_downloader.downloader.all.dl_arsya_biz_id import _DlArsyaBizIdDownloader
from social_media_downloader.downloader.facebook.url_parser import FacebookUrlParser
from social_media_downloader.downloader.instagram.url_parser import InstagramUrlParser
from social_media_downloader.downloader.tiktok.url_parser import TiktokUrlParser
from file_downloader_easy import FileDownloader


class SocialMediaDownloader:
    """
    Class to simplify the download of Tiktok,
    Instagram and Facebook videos.

    You can use it within a context like this:
    ```
    async with SocialMediaDownloader() as social_media_downloader:
        await social_media_downloader.tiktok.download_video(...)
        await social_media_downloader.instagram.download_video(...)
        await social_media_downloader.facebook.download_video(...)
    ```
    """

    def __init__(
        self,
        do_follow_redirects: bool = False
    ):
        self._file_downloader: FileDownloader = FileDownloader(
            do_follow_redirects = do_follow_redirects
        )
        """
        *For internal use only*

        The `FileDownloader` instance that will navigate
        download the files we need.
        """
        
        self.facebook: '_FacebookDownloader' = _FacebookDownloader(self)
        """
        Shortcut to the functionality related to
        Facebook.
        """
        self.instagram: '_InstagramDownloader' = _InstagramDownloader(self)
        """
        Shortcut to the functionality related to
        Instagram.
        """
        self.tiktok: '_TiktokDownloader' = _TiktokDownloader(self)
        """
        Shortcut to the functionality related to
        Tiktok.
        """

        # Experimental and not used yet
        self.snapsave: '_SnapsaveDownloader' = _SnapsaveDownloader(self)
        """
        Shortcut to the Snapsave app functionality,
        that is able to download a lot of different
        types of videos.
        """
        self.dl_arsya_biz_id: '_DlArsyaBizIdDownloader' = _DlArsyaBizIdDownloader(self)
        """
        Shortcut to the DlArsyaBizId app functionality,
        that is able to download a lot of different
        types of videos with its own API, which is
        connecting with the Snapsave app in the
        background.
        """

    async def __aenter__(
        self
    ):
        await self._file_downloader.__aenter__()

        return self

    async def __aexit__(
        self,
        exc_type,
        exc,
        tb
    ):
        return await self._file_downloader.__aexit__(
            exc_type,
            exc,
            tb
        )

    async def download_video(
        self,
        url: str,
        output_filename: str
    ):
        """
        Download the video from the `url` given and
        save it locally as `output_filename`. The
        `url` must be a valid and accepted Facebook,
        Instagram or Tiktok url.
        """
        downloaders = (
            (FacebookUrlParser, self.facebook),
            (InstagramUrlParser, self.instagram),
            (TiktokUrlParser, self.tiktok),
        )

        for parser, downloader in downloaders:
            if parser.is_valid(url):
                # Get url to download
                download_url = await downloader.get_download_url(
                    url = url,
                    # TODO: This 'output_filename' is not needed
                    output_filename = output_filename
                )

                # Download it
                file_resource = await self._file_downloader._get_file(
                    url = download_url,
                    output_filename = output_filename
                    # TODO: Allow it when 'Output' is public
                    # output_filename = Output.get_filename(
                    #     filename = output_filename,
                    #     file_extension = VideoFileExtension
                    # )
                )

                file_resource.source_url = url

                return file_resource 

        raise ValueError(f'The "url" provided is not a valid Facebook, Instagram nor Tiktok url: {url}')
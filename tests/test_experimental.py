import pytest


@pytest.mark.additional
@pytest.mark.asyncio
async def test_instagram_downloader():
    """
    Due to changes in the endpoint we need
    to make sure that we update the code
    and it is working for the new version.
    """
    from social_media_downloader_easy import SocialMediaDownloader

    test_filename = 'test_files/test_instagram_downloader.mp4'

    await SocialMediaDownloader().download_video(
        url = 'https://www.instagram.com/reel/DHtsmGHTOn4/',
        output_filename = test_filename
    )

    assert False


# @pytest.mark.additional
# @pytest.mark.asyncio
# async def test_snapsave_app():
#     from social_media_downloader_easy.downloader.all.snapsaveapp import _SnapsaveDownloader
#     from tests.common import INSTAGRAM_REEL_URL

#     download_url = _SnapsaveDownloader().download(INSTAGRAM_REEL_URL)

#     print(download_url)

#     # assert False


# # TODO: Too many requests sometimes...
# @pytest.mark.additional
# @pytest.mark.asyncio
# async def test_dl_arsya_biz_id():
#     from social_media_downloader_easy.downloader.all.dl_arsya_biz_id import _DlArsyaBizIdDownloader
#     from tests.common import INSTAGRAM_REEL_URL

#     download_url = await _DlArsyaBizIdDownloader().get_download_url(INSTAGRAM_REEL_URL)

#     print(download_url)

#     # assert False
    
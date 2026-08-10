import pytest


@pytest.mark.additional
@pytest.mark.asyncio
async def test_snapsave_app():
    from social_media_downloader.downloader.all.snapsaveapp import _SnapsaveDownloader
    from tests.common import INSTAGRAM_REEL_URL

    download_url = _SnapsaveDownloader().download(INSTAGRAM_REEL_URL)

    print(download_url)

    assert False


# TODO: Too many requests sometimes...
@pytest.mark.additional
@pytest.mark.asyncio
async def test_dl_arsya_biz_id():
    from social_media_downloader.downloader.all.dl_arsya_biz_id import _DlArsyaBizIdDownloader
    from tests.common import INSTAGRAM_REEL_URL

    download_url = await _DlArsyaBizIdDownloader().get_download_url(INSTAGRAM_REEL_URL)

    print(download_url)
    
    assert False
    
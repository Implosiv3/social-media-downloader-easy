from social_media_downloader_easy.metadata_fetcher import MetadataFetcher

import pytest


@pytest.mark.additional
@pytest.mark.asyncio
async def test_get_metadata():
    from tests.common import TIKTOK_VIDEO_SHORT_URL

    metadata = MetadataFetcher().tiktok.get_metadata(TIKTOK_VIDEO_SHORT_URL)

    assert metadata.id == '7586250089434221846'
    assert metadata.username == 'laylaloutfi'
    assert metadata.title == 'Exploring the Beauty and Kindness of Cambodia'
    assert metadata.description == 'Cambodia has been so quiet and just wanna assure people it is safe, beautiful and full of the kindest locals you will ever meet \U0001faf6\U0001faf6 will continue to try make content but this holiday season is hitting me hard lol so I’m just taking it easy rn hence the puffy eyes #cambodia #kohrong #femaletravel #solotravel #travelcambodia'

    
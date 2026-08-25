from social_media_downloader_easy.metadata_fetcher import MetadataFetcher

import pytest


@pytest.mark.additional
@pytest.mark.asyncio
async def test_get_metadata():
    from tests.common import TIKTOK_VIDEO_SHORT_URL
    from datetime import datetime, timezone

    metadata_fetcher = MetadataFetcher()

    metadata = metadata_fetcher.tiktok.get_metadata(TIKTOK_VIDEO_SHORT_URL)

    # assert metadata.id == '7586250089434221846'
    assert metadata.author_name == 'Layla Loutfi'
    assert metadata.author_username == 'laylaloutfi'
    assert metadata.author_url == 'https://www.tiktok.com/@laylaloutfi'
    # assert metadata.title == 'Exploring the Beauty and Kindness of Cambodia'
    assert metadata.description == 'Cambodia has been so quiet and just wanna assure people it is safe, beautiful and full of the kindest locals you will ever meet \U0001faf6\U0001faf6 will continue to try make content but this holiday season is hitting me hard lol so I’m just taking it easy rn hence the puffy eyes #cambodia #kohrong #femaletravel #solotravel #travelcambodia '

    published_at = metadata_fetcher.tiktok.get_publication_date(TIKTOK_VIDEO_SHORT_URL)

    # '2025-12-21 10:04:51+00:00'
    assert published_at == datetime(
        2025,
        12,
        21,
        10,
        4,
        51,
        tzinfo = timezone.utc,
    )

    
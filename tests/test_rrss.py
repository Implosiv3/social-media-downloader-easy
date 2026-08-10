from social_media_downloader_easy.downloader import SocialMediaDownloader
from tests.common import (
    TIKTOK_VIDEO_LONG_URL,
    TIKTOK_VIDEO_SHORT_URL,
    # Instagram
    INSTAGRAM_REEL_URL,
    # These commented are not accepted by the current method
    # INSTAGRAM_SHARED_REEL_URL,
    # INSTAGRAM_REELS_URL,
    INSTAGRAM_POST_URL,
    # Facebook
    FACEBOOK_VIDEO_URL,
    FACEBOOK_REEL_URL,
    FACEBOOK_SHARED_REEL_URL,
    FACEBOOK_VIDEO_WATCH_URL,
    FACEBOOK_VIDEO_FOO_2_URL,
    FACEBOOK_VIDEO_FOO_URL
)

import pytest


@pytest.mark.additional
@pytest.mark.asyncio
async def test_tiktok():
    TIKTOK_URLS = [
        TIKTOK_VIDEO_LONG_URL,
        TIKTOK_VIDEO_SHORT_URL
    ]

    async with SocialMediaDownloader(do_follow_redirects = True) as social_media_downloader:
        for index, url in enumerate(TIKTOK_URLS):
            output_filename = f'test_files/tiktok_{str(index)}.mp4'

            tiktok_video_downloaded = await social_media_downloader.tiktok.download_video(
                url = url,
                output_filename = output_filename
            )

            assert tiktok_video_downloaded.filename == output_filename


@pytest.mark.additional
@pytest.mark.asyncio
async def test_instagram():
    INSTAGRAM_URLS = [
        INSTAGRAM_REEL_URL,
        # These commented are not accepted by the current method
        # INSTAGRAM_SHARED_REEL_URL,
        # INSTAGRAM_REELS_URL,
        INSTAGRAM_POST_URL
    ]

    async with SocialMediaDownloader(do_follow_redirects = True) as social_media_downloader:
        for index, url in enumerate(INSTAGRAM_URLS):
            output_filename = f'test_files/instagram_{str(index)}.mp4'

            instagram_video_downloaded = await social_media_downloader.instagram.download_video(
                url = url,
                output_filename = output_filename
            )

            assert instagram_video_downloaded.filename == output_filename


@pytest.mark.additional
@pytest.mark.asyncio
async def test_facebook():
    FACEBOOK_URLS = [
        FACEBOOK_VIDEO_URL,
        FACEBOOK_REEL_URL,
        FACEBOOK_SHARED_REEL_URL,
        FACEBOOK_VIDEO_WATCH_URL,
        FACEBOOK_VIDEO_FOO_2_URL,
        FACEBOOK_VIDEO_FOO_URL
    ]

    async with SocialMediaDownloader(do_follow_redirects = True) as social_media_downloader:
        for index, url in enumerate(FACEBOOK_URLS):
            output_filename = f'test_files/facebook_{str(index)}.mp4'

            facebook_video_downloaded = await social_media_downloader.facebook.download_video(
                url = url,
                output_filename = output_filename
            )

            assert facebook_video_downloaded.filename == output_filename


@pytest.mark.additional
@pytest.mark.asyncio
async def test_mixed():
    URLS = [
        TIKTOK_VIDEO_LONG_URL,
        FACEBOOK_VIDEO_URL,
        INSTAGRAM_REEL_URL,
    ]

    async with SocialMediaDownloader(do_follow_redirects = True) as social_media_downloader:
        for index, url in enumerate(URLS):
            output_filename = f'test_files/mixed_{str(index)}.mp4'

            mixed_video_downloaded = await social_media_downloader.download_video(
                url = url,
                output_filename = output_filename
            )

            assert mixed_video_downloaded.filename == output_filename


"""
A simple test to verify that pytes is working and
the tests are being detected.
"""
import pytest


@pytest.mark.additional
def test_platform_youtube():
    from social_media_downloader_easy.platform.youtube.dataclasses import YoutubeVideoUrl
    from social_media_downloader_easy.platform.youtube.enums import YoutubeUrlType

    VIDEO_ID = 'ZbsOEWDGZYQ'
    VIDEO_WATCH_FORMAT = f'https://www.youtube.com/watch?v={VIDEO_ID}'
    VIDEO_V_FORMAT = f'https://www.youtube.com/v/{VIDEO_ID}'
    VIDEO_SHORT_FORMAT = f'https://youtu.be/{VIDEO_ID}'
    VIDEO_SHORTS_FORMAT = f'https://www.youtube.com/shorts/{VIDEO_ID}'
    VIDEO_EMBED_FORMAT = f'https://www.youtube.com/embed/{VIDEO_ID}'

    youtube_video_url = YoutubeVideoUrl.parse(VIDEO_WATCH_FORMAT)
    assert youtube_video_url.url_type == YoutubeUrlType.WATCH
    assert youtube_video_url.video_id == VIDEO_ID

    youtube_video_url = YoutubeVideoUrl.parse(VIDEO_V_FORMAT)
    assert youtube_video_url.url_type == YoutubeUrlType.V
    assert youtube_video_url.video_id == VIDEO_ID

    youtube_video_url = YoutubeVideoUrl.parse(VIDEO_SHORT_FORMAT)
    assert youtube_video_url.url_type == YoutubeUrlType.SHORT_URL
    assert youtube_video_url.video_id == VIDEO_ID

    # TODO: Shorts is not accepted
    youtube_video_url = YoutubeVideoUrl.parse(VIDEO_SHORTS_FORMAT)
    assert youtube_video_url.url_type == YoutubeUrlType.SHORTS
    assert youtube_video_url.video_id == VIDEO_ID

    youtube_video_url = YoutubeVideoUrl.parse(VIDEO_EMBED_FORMAT)
    assert youtube_video_url.url_type == YoutubeUrlType.EMBED
    assert youtube_video_url.video_id == VIDEO_ID

    # From id
    youtube_video_url = YoutubeVideoUrl.from_video_id(VIDEO_ID)
    assert youtube_video_url.url_type == YoutubeUrlType.WATCH
    assert youtube_video_url.video_id == VIDEO_ID


@pytest.mark.additional
def test_platform_tiktok():
    from social_media_downloader_easy.platform.tiktok.dataclasses import TiktokVideoUrl
    from social_media_downloader_easy.platform.tiktok.enums import TikTokUrlType

    VIDEO_ID = '7669879089280339232'
    VIDEO_SHORT_CODE = 'ZGdxm6n7v'
    VIDEO_URL = f'https://www.tiktok.com/@voyepic/video/{VIDEO_ID}'
    VIDEO_SHORT_URL = f'https://vm.tiktok.com/{VIDEO_SHORT_CODE}'

    tiktok_video_url = TiktokVideoUrl.parse(VIDEO_URL)
    assert tiktok_video_url.url_type == TikTokUrlType.VIDEO
    assert tiktok_video_url.video_id == VIDEO_ID
    assert tiktok_video_url.username == 'voyepic'

    tiktok_video_url = TiktokVideoUrl.parse(VIDEO_SHORT_URL)
    assert tiktok_video_url.url_type == TikTokUrlType.SHORT_URL
    assert tiktok_video_url.video_id == None
    # This will perform the redirect
    assert tiktok_video_url.username == 'voyepic'
    assert tiktok_video_url.video_id == VIDEO_ID
    assert tiktok_video_url.long_url == VIDEO_URL
    
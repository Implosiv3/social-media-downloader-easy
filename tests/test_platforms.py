"""
A simple test to verify that pytes is working and
the tests are being detected.
"""
import pytest


@pytest.mark.additional
def test_platform_youtube():
    from social_media_downloader_easy.platform.youtube.dataclasses import YoutubeVideoUrl
    from social_media_downloader_easy.platform.youtube.enums import YoutubeUrlType
    from social_media_downloader_easy.platform.youtube.regex import YoutubeVideoUrlRegularExpression

    VIDEO_ID = 'ZbsOEWDGZYQ'
    VIDEO_WATCH_FORMAT = f'https://www.youtube.com/watch?v={VIDEO_ID}'
    VIDEO_V_FORMAT = f'https://www.youtube.com/v/{VIDEO_ID}'
    VIDEO_SHORT_FORMAT = f'https://youtu.be/{VIDEO_ID}'
    VIDEO_SHORTS_FORMAT = f'https://www.youtube.com/shorts/{VIDEO_ID}'
    VIDEO_EMBED_FORMAT = f'https://www.youtube.com/embed/{VIDEO_ID}'

    assert YoutubeVideoUrlRegularExpression.YOUTUBE_WATCH_REGEX.is_valid(VIDEO_WATCH_FORMAT) == True
    assert YoutubeVideoUrlRegularExpression.YOUTUBE_V_REGEX.is_valid(VIDEO_V_FORMAT) == True
    assert YoutubeVideoUrlRegularExpression.YOUTUBE_SHORT_URL_REGEX.is_valid(VIDEO_SHORT_FORMAT) == True
    assert YoutubeVideoUrlRegularExpression.YOUTUBE_SHORTS_REGEX.is_valid(VIDEO_SHORTS_FORMAT) == True
    assert YoutubeVideoUrlRegularExpression.YOUTUBE_EMBED_REGEX.is_valid(VIDEO_EMBED_FORMAT) == True

    assert YoutubeVideoUrl.is_valid(VIDEO_WATCH_FORMAT) == True
    assert YoutubeVideoUrl.is_valid(VIDEO_V_FORMAT) == True
    assert YoutubeVideoUrl.is_valid(VIDEO_SHORT_FORMAT) == True
    assert YoutubeVideoUrl.is_valid(VIDEO_SHORTS_FORMAT) == True
    assert YoutubeVideoUrl.is_valid(VIDEO_EMBED_FORMAT) == True

    youtube_video_url = YoutubeVideoUrl(VIDEO_WATCH_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.WATCH
    assert youtube_video_url.video_id == VIDEO_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={VIDEO_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{VIDEO_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{VIDEO_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{VIDEO_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{VIDEO_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{VIDEO_ID}'

    youtube_video_url = YoutubeVideoUrl(VIDEO_V_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.V
    assert youtube_video_url.video_id == VIDEO_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={VIDEO_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{VIDEO_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{VIDEO_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{VIDEO_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{VIDEO_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{VIDEO_ID}'

    youtube_video_url = YoutubeVideoUrl(VIDEO_SHORT_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.SHORT_URL
    assert youtube_video_url.video_id == VIDEO_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={VIDEO_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{VIDEO_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{VIDEO_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{VIDEO_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{VIDEO_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{VIDEO_ID}'

    youtube_video_url = YoutubeVideoUrl(VIDEO_SHORTS_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.SHORTS
    assert youtube_video_url.video_id == VIDEO_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={VIDEO_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{VIDEO_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{VIDEO_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{VIDEO_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{VIDEO_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{VIDEO_ID}'

    youtube_video_url = YoutubeVideoUrl(VIDEO_EMBED_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.EMBED
    assert youtube_video_url.video_id == VIDEO_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={VIDEO_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{VIDEO_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{VIDEO_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{VIDEO_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{VIDEO_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{VIDEO_ID}'

    # From id
    youtube_video_url = YoutubeVideoUrl.from_video_id(VIDEO_ID)
    assert youtube_video_url._url_type == YoutubeUrlType.WATCH
    assert youtube_video_url.video_id == VIDEO_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={VIDEO_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{VIDEO_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{VIDEO_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{VIDEO_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{VIDEO_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{VIDEO_ID}'


@pytest.mark.additional
def test_platform_tiktok():
    from social_media_downloader_easy.platform.tiktok.dataclasses import TiktokVideoUrl
    from social_media_downloader_easy.platform.tiktok.enums import TikTokUrlType
    from social_media_downloader_easy.platform.tiktok.regex import TiktokVideoUrlRegularExpression

    VIDEO_ID = '7669879089280339232'
    VIDEO_SHORTCODE = 'ZGdxm6n7v'
    VIDEO_URL = f'https://www.tiktok.com/@voyepic/video/{VIDEO_ID}'
    VIDEO_SHORT_URL = f'https://vm.tiktok.com/{VIDEO_SHORTCODE}'

    assert TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_ID_REGEX.is_valid(VIDEO_ID) == True
    assert TiktokVideoUrlRegularExpression.TIKTOK_SHORTCODE_REGEX.is_valid(VIDEO_SHORTCODE) == True
    assert TiktokVideoUrlRegularExpression.TIKTOK_VIDEO_URL_REGEX.is_valid(VIDEO_URL) == True
    assert TiktokVideoUrlRegularExpression.TIKTOK_SHORT_URL_REGEX.is_valid(VIDEO_SHORT_URL) == True

    assert TiktokVideoUrl.is_valid(VIDEO_URL)
    assert TiktokVideoUrl.is_valid(VIDEO_SHORT_URL)

    tiktok_video_url = TiktokVideoUrl(VIDEO_URL)
    assert tiktok_video_url._url_type == TikTokUrlType.VIDEO
    assert tiktok_video_url.video_id == VIDEO_ID
    assert tiktok_video_url.username == 'voyepic'
    assert tiktok_video_url.long_url == VIDEO_URL

    # This will perform the redirect
    tiktok_video_url = TiktokVideoUrl(VIDEO_SHORT_URL)
    assert tiktok_video_url._url_type == TikTokUrlType.SHORT_URL
    assert tiktok_video_url.username == 'voyepic'
    assert tiktok_video_url.video_id == VIDEO_ID
    assert tiktok_video_url.long_url == VIDEO_URL

    tiktok_video_url = TiktokVideoUrl.from_video_id(VIDEO_ID)
    assert tiktok_video_url._url_type == TikTokUrlType.VIDEO
    assert tiktok_video_url.username == 'voyepic'
    assert tiktok_video_url.video_id == VIDEO_ID
    assert tiktok_video_url.long_url == VIDEO_URL

    tiktok_video_url = TiktokVideoUrl.from_shortcode(VIDEO_SHORTCODE)
    assert tiktok_video_url._url_type == TikTokUrlType.SHORT_URL
    assert tiktok_video_url.username == 'voyepic'
    assert tiktok_video_url.video_id == VIDEO_ID
    assert tiktok_video_url.long_url == VIDEO_URL
    
import pytest


@pytest.mark.additional
def test_platform_facebook():
    from social_media_downloader_easy.platform.facebook.dataclasses import FacebookPostUrl
    from social_media_downloader_easy.platform.facebook.enums import FacebookUrlType
    from social_media_downloader_easy.platform.facebook.regex import FacebookPostUrlRegularExpression

    VIDEO_ID = '875491608967954'
    SHORTCODE = '1L6vVe9TjZ'
    VIDEO_WATCH_URL = f'https://www.facebook.com/watch/?v={VIDEO_ID}'
    VIDEO_URL = f'https://www.facebook.com/NONAME/videos/{VIDEO_ID}'
    VIDEO_REEL_URL = f'https://www.facebook.com/reel/{VIDEO_ID}'
    # TODO: This one is apparently not the same shortcode
    # VIDEO_SHORT_URL = f'https://fb.watch/{SHORTCODE}'
    VIDEO_SHARE_URL = f'https://www.facebook.com/share/v/{SHORTCODE}'
    REEL_SHARE_URL = f'https://www.facebook.com/share/r/{SHORTCODE}'

    # Regular expressions
    assert FacebookPostUrlRegularExpression.FACEBOOK_POST_ID_REGEX.is_valid(VIDEO_ID) == True
    assert FacebookPostUrlRegularExpression.FACEBOOK_SHORTCODE_REGEX.is_valid(SHORTCODE) == True
    assert FacebookPostUrlRegularExpression.FACEBOOK_WATCH_URL_REGEX.is_valid(VIDEO_WATCH_URL) == True
    assert FacebookPostUrlRegularExpression.FACEBOOK_VIDEO_URL_REGEX.is_valid(VIDEO_URL) == True
    assert FacebookPostUrlRegularExpression.FACEBOOK_REEL_URL_REGEX.is_valid(VIDEO_REEL_URL) == True
    # assert FacebookPostUrlRegularExpression.FACEBOOK_SHORT_URL_REGEX.is_valid(VIDEO_SHORT_URL) == True
    assert FacebookPostUrlRegularExpression.FACEBOOK_SHARE_VIDEO_URL_REGEX.is_valid(VIDEO_SHARE_URL) == True
    assert FacebookPostUrlRegularExpression.FACEBOOK_SHARE_REEL_URL_REGEX.is_valid(REEL_SHARE_URL) == True

    # URL validation
    assert FacebookPostUrl.is_valid(VIDEO_WATCH_URL) == True
    assert FacebookPostUrl.is_valid(VIDEO_URL) == True
    assert FacebookPostUrl.is_valid(VIDEO_REEL_URL) == True
    # TODO: It doesn't work in incognito
    # assert FacebookPostUrl.is_valid(VIDEO_SHORT_URL) == True
    assert FacebookPostUrl.is_valid(VIDEO_SHARE_URL) == True
    assert FacebookPostUrl.is_valid(REEL_SHARE_URL) == True

    # Watch URL
    facebook_video_url = FacebookPostUrl(VIDEO_WATCH_URL)
    assert facebook_video_url._url_type == FacebookUrlType.WATCH
    assert facebook_video_url.id == VIDEO_ID
    assert facebook_video_url.watch_url == VIDEO_WATCH_URL
    assert facebook_video_url.reel_url == f'https://www.facebook.com/reel/{VIDEO_ID}'

    # Video URL
    facebook_video_url = FacebookPostUrl(VIDEO_URL)
    assert facebook_video_url._url_type == FacebookUrlType.VIDEO
    assert facebook_video_url.id == VIDEO_ID
    assert facebook_video_url.watch_url == f'https://www.facebook.com/watch/?v={VIDEO_ID}'
    assert facebook_video_url.reel_url == f'https://www.facebook.com/reel/{VIDEO_ID}'

    # Reel URL
    facebook_video_url = FacebookPostUrl(VIDEO_REEL_URL)
    assert facebook_video_url._url_type == FacebookUrlType.REEL
    assert facebook_video_url.id == VIDEO_ID
    assert facebook_video_url.watch_url == f'https://www.facebook.com/watch/?v={VIDEO_ID}'
    assert facebook_video_url.reel_url == VIDEO_REEL_URL

    # # Short URL
    # facebook_video_url = FacebookPostUrl(VIDEO_SHORT_URL)
    # assert facebook_video_url._url_type == FacebookUrlType.SHORT_URL
    # assert facebook_video_url.id is None

    # Share video URL
    facebook_video_url = FacebookPostUrl(VIDEO_SHARE_URL)
    assert facebook_video_url._url_type == FacebookUrlType.SHARE_VIDEO
    assert facebook_video_url.id == VIDEO_ID
    assert facebook_video_url.watch_url == f'https://www.facebook.com/watch/?v={VIDEO_ID}'
    assert facebook_video_url.reel_url == f'https://www.facebook.com/reel/{VIDEO_ID}'
    assert facebook_video_url.long_url == f'https://www.facebook.com/reel/{VIDEO_ID}'

    # Share reel URL
    facebook_video_url = FacebookPostUrl(REEL_SHARE_URL)
    assert facebook_video_url._url_type == FacebookUrlType.SHARE_REEL
    assert facebook_video_url.id == VIDEO_ID
    assert facebook_video_url.watch_url == f'https://www.facebook.com/watch/?v={VIDEO_ID}'
    assert facebook_video_url.reel_url == f'https://www.facebook.com/reel/{VIDEO_ID}'
    assert facebook_video_url.long_url == f'https://www.facebook.com/reel/{VIDEO_ID}'

    # From video ID
    facebook_video_url = FacebookPostUrl.from_id(VIDEO_ID)
    assert facebook_video_url._url_type == FacebookUrlType.WATCH
    assert facebook_video_url.id == VIDEO_ID
    assert facebook_video_url.watch_url == f'https://www.facebook.com/watch/?v={VIDEO_ID}'
    assert facebook_video_url.reel_url == f'https://www.facebook.com/reel/{VIDEO_ID}'
    assert facebook_video_url.long_url == f'https://www.facebook.com/reel/{VIDEO_ID}'

    # From shortcode
    facebook_video_url = FacebookPostUrl.from_shortcode(SHORTCODE)
    assert facebook_video_url._url_type == FacebookUrlType.SHARE_VIDEO
    assert facebook_video_url.id == VIDEO_ID
    assert facebook_video_url.watch_url == f'https://www.facebook.com/watch/?v={VIDEO_ID}'
    assert facebook_video_url.reel_url == f'https://www.facebook.com/reel/{VIDEO_ID}'
    assert facebook_video_url.long_url == f'https://www.facebook.com/reel/{VIDEO_ID}'
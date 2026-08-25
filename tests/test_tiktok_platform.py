import pytest


@pytest.mark.additional
def test_platform_tiktok():
    from social_media_downloader_easy.platform.tiktok.dataclasses import TiktokPostUrl
    from social_media_downloader_easy.platform.tiktok.enums import TikTokUrlType
    from social_media_downloader_easy.platform.tiktok.regex import TiktokPostUrlRegularExpression

    POST_ID = '7669879089280339232'
    POST_SHORTCODE = 'ZGdxm6n7v'
    POST_URL = f'https://www.tiktok.com/@voyepic/video/{POST_ID}'
    POST_SHORT_URL = f'https://vm.tiktok.com/{POST_SHORTCODE}'

    assert TiktokPostUrlRegularExpression.TIKTOK_POST_ID_REGEX.is_valid(POST_ID) == True
    assert TiktokPostUrlRegularExpression.TIKTOK_SHORTCODE_REGEX.is_valid(POST_SHORTCODE) == True
    assert TiktokPostUrlRegularExpression.TIKTOK_POST_URL_REGEX.is_valid(POST_URL) == True
    assert TiktokPostUrlRegularExpression.TIKTOK_SHORT_URL_REGEX.is_valid(POST_SHORT_URL) == True

    assert TiktokPostUrl.is_valid(POST_URL)
    assert TiktokPostUrl.is_valid(POST_SHORT_URL)

    tiktok_video_url = TiktokPostUrl(POST_URL)
    assert tiktok_video_url._url_type == TikTokUrlType.VIDEO
    assert tiktok_video_url.id == POST_ID
    assert tiktok_video_url.username == 'voyepic'
    assert tiktok_video_url.long_url == POST_URL

    # This will perform the redirect
    tiktok_video_url = TiktokPostUrl(POST_SHORT_URL)
    assert tiktok_video_url._url_type == TikTokUrlType.SHORT_URL
    assert tiktok_video_url.username == 'voyepic'
    assert tiktok_video_url.id == POST_ID
    assert tiktok_video_url.long_url == POST_URL

    # TODO: This is not working
    # tiktok_video_url = TiktokPostUrl.from_id(POST_ID)
    # assert tiktok_video_url._url_type == TikTokUrlType.VIDEO
    # assert tiktok_video_url.username == 'voyepic'
    # assert tiktok_video_url.id == POST_ID
    # assert tiktok_video_url.long_url == POST_URL

    tiktok_video_url = TiktokPostUrl.from_shortcode(POST_SHORTCODE)
    assert tiktok_video_url._url_type == TikTokUrlType.SHORT_URL
    assert tiktok_video_url.username == 'voyepic'
    assert tiktok_video_url.id == POST_ID
    assert tiktok_video_url.long_url == POST_URL
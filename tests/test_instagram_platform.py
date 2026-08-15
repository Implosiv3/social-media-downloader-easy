import pytest


@pytest.mark.additional
def test_platform_instagram():
    from social_media_downloader_easy.platform.instagram.dataclasses import InstagramPostUrl
    from social_media_downloader_easy.platform.instagram.enums import InstagramUrlType
    from social_media_downloader_easy.platform.instagram.regex import InstagramPostUrlRegularExpression

    POST_ID = 'DJx123ABC'
    POST_REEL_URL = f'https://www.instagram.com/reel/{POST_ID}'
    POST_POST_URL = f'https://www.instagram.com/p/{POST_ID}'
    POST_REELS_URL = f'https://www.instagram.com/reels/{POST_ID}'
    POST_TV_URL = f'https://www.instagram.com/tv/{POST_ID}'

    assert InstagramPostUrlRegularExpression.INSTAGRAM_ID_REGEX.is_valid(POST_ID) == True
    assert InstagramPostUrlRegularExpression.INSTAGRAM_REEL_URL_REGEX.is_valid(POST_REEL_URL) == True
    assert InstagramPostUrlRegularExpression.INSTAGRAM_POST_URL_REGEX.is_valid(POST_POST_URL) == True
    assert InstagramPostUrlRegularExpression.INSTAGRAM_REELS_URL_REGEX.is_valid(POST_REELS_URL) == True
    assert InstagramPostUrlRegularExpression.INSTAGRAM_TV_URL_REGEX.is_valid(POST_TV_URL) == True

    assert InstagramPostUrl.is_valid(POST_REEL_URL) == True
    assert InstagramPostUrl.is_valid(POST_POST_URL) == True
    assert InstagramPostUrl.is_valid(POST_REELS_URL) == True
    assert InstagramPostUrl.is_valid(POST_TV_URL) == True

    instagram_video_url = InstagramPostUrl(POST_REEL_URL)
    assert instagram_video_url._url_type == InstagramUrlType.REEL
    assert instagram_video_url.id == POST_ID
    assert instagram_video_url.reel_url == POST_REEL_URL
    assert instagram_video_url.post_url == POST_POST_URL
    assert instagram_video_url.reels_url == POST_REELS_URL
    assert instagram_video_url.tv_url == POST_TV_URL

    instagram_video_url = InstagramPostUrl(POST_POST_URL)
    assert instagram_video_url._url_type == InstagramUrlType.POST
    assert instagram_video_url.id == POST_ID
    assert instagram_video_url.reel_url == POST_REEL_URL
    assert instagram_video_url.post_url == POST_POST_URL
    assert instagram_video_url.reels_url == POST_REELS_URL
    assert instagram_video_url.tv_url == POST_TV_URL

    instagram_video_url = InstagramPostUrl(POST_REELS_URL)
    assert instagram_video_url._url_type == InstagramUrlType.REELS
    assert instagram_video_url.id == POST_ID
    assert instagram_video_url.reel_url == POST_REEL_URL
    assert instagram_video_url.post_url == POST_POST_URL
    assert instagram_video_url.reels_url == POST_REELS_URL
    assert instagram_video_url.tv_url == POST_TV_URL

    instagram_video_url = InstagramPostUrl(POST_TV_URL)
    assert instagram_video_url._url_type == InstagramUrlType.TV
    assert instagram_video_url.id == POST_ID
    assert instagram_video_url.reel_url == POST_REEL_URL
    assert instagram_video_url.post_url == POST_POST_URL
    assert instagram_video_url.reels_url == POST_REELS_URL
    assert instagram_video_url.tv_url == POST_TV_URL

    # From id
    instagram_video_url = InstagramPostUrl.from_id(POST_ID)
    assert instagram_video_url._url_type == InstagramUrlType.REEL
    assert instagram_video_url.id == POST_ID
    assert instagram_video_url.reel_url == POST_REEL_URL
    assert instagram_video_url.post_url == POST_POST_URL
    assert instagram_video_url.reels_url == POST_REELS_URL
    assert instagram_video_url.tv_url == POST_TV_URL
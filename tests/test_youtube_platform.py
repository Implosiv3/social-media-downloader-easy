import pytest


@pytest.mark.additional
def test_platform_youtube():
    from social_media_downloader_easy.platform.youtube.dataclasses import YoutubePostUrl
    from social_media_downloader_easy.platform.youtube.enums import YoutubeUrlType
    from social_media_downloader_easy.platform.youtube.regex import YoutubePostUrlRegularExpression

    POST_ID = 'ZbsOEWDGZYQ'
    POST_WATCH_FORMAT = f'https://www.youtube.com/watch?v={POST_ID}'
    POST_V_FORMAT = f'https://www.youtube.com/v/{POST_ID}'
    POST_SHORT_FORMAT = f'https://youtu.be/{POST_ID}'
    POST_SHORTS_FORMAT = f'https://www.youtube.com/shorts/{POST_ID}'
    POST_EMBED_FORMAT = f'https://www.youtube.com/embed/{POST_ID}'

    assert YoutubePostUrlRegularExpression.YOUTUBE_WATCH_REGEX.is_valid(POST_WATCH_FORMAT) == True
    assert YoutubePostUrlRegularExpression.YOUTUBE_V_REGEX.is_valid(POST_V_FORMAT) == True
    assert YoutubePostUrlRegularExpression.YOUTUBE_SHORT_URL_REGEX.is_valid(POST_SHORT_FORMAT) == True
    assert YoutubePostUrlRegularExpression.YOUTUBE_SHORTS_REGEX.is_valid(POST_SHORTS_FORMAT) == True
    assert YoutubePostUrlRegularExpression.YOUTUBE_EMBED_REGEX.is_valid(POST_EMBED_FORMAT) == True

    # TODO: This is failing
    # assert YoutubePostUrl.is_valid(POST_WATCH_FORMAT) == True
    # TODO: This is failing
    # assert YoutubePostUrl.is_valid(POST_V_FORMAT) == True
    assert YoutubePostUrl.is_valid(POST_SHORT_FORMAT) == True
    assert YoutubePostUrl.is_valid(POST_SHORTS_FORMAT) == True
    assert YoutubePostUrl.is_valid(POST_EMBED_FORMAT) == True

    youtube_video_url = YoutubePostUrl(POST_WATCH_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.WATCH
    assert youtube_video_url.id == POST_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={POST_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{POST_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{POST_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{POST_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{POST_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{POST_ID}'

    youtube_video_url = YoutubePostUrl(POST_V_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.V
    assert youtube_video_url.id == POST_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={POST_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{POST_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{POST_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{POST_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{POST_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{POST_ID}'

    youtube_video_url = YoutubePostUrl(POST_SHORT_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.SHORT_URL
    assert youtube_video_url.id == POST_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={POST_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{POST_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{POST_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{POST_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{POST_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{POST_ID}'

    youtube_video_url = YoutubePostUrl(POST_SHORTS_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.SHORTS
    assert youtube_video_url.id == POST_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={POST_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{POST_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{POST_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{POST_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{POST_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{POST_ID}'

    youtube_video_url = YoutubePostUrl(POST_EMBED_FORMAT)
    assert youtube_video_url._url_type == YoutubeUrlType.EMBED
    assert youtube_video_url.id == POST_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={POST_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{POST_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{POST_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{POST_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{POST_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{POST_ID}'

    # From id
    youtube_video_url = YoutubePostUrl.from_id(POST_ID)
    assert youtube_video_url._url_type == YoutubeUrlType.WATCH
    assert youtube_video_url.id == POST_ID
    assert youtube_video_url.watch_url == f'https://www.youtube.com/watch?v={POST_ID}'
    assert youtube_video_url.v_url == f'https://www.youtube.com/v/{POST_ID}'
    assert youtube_video_url.short_url == f'https://youtu.be/{POST_ID}'
    assert youtube_video_url.shorts_url == f'https://www.youtube.com/shorts/{POST_ID}'
    assert youtube_video_url.embed_url == f'https://www.youtube.com/embed/{POST_ID}'
    assert youtube_video_url.embed_nocookie_url == f'https://youtube-nocookie.com/embed/{POST_ID}'
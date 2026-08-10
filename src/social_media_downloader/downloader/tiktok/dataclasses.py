"""
You have some information at the end of this
file.
"""
from dataclasses import dataclass


@dataclass(slots = True)
class TiktokUrl:
    """
    Dataclass to hold the information about
    a TikTok video URL.
    """

    username: str
    """
    The user who the video belongs to.
    """

    video_id: str
    """
    The id of the video.
    """

    url: str
    """
    The long TikTok URL of that video.
    """


@dataclass(slots = True)
class TikTokAuthor:

    id: str
    """
    The id of the author.
    """
    unique_id: str
    nickname: str
    avatar: str


@dataclass(slots = True)
class TikTokMusicInfo:

    id: str
    title: str
    play: str
    cover: str
    author: str
    original: bool
    duration: int
    album: str


@dataclass(slots = True)
class TikTokVideo:
    """
    *Dataclass*

    A dataclass to include the information of a Tiktok
    video extracted by using the next platform:
    - `https://tikwm.com/api/`
    """

    id: str
    region: str
    title: str

    cover: str
    origin_cover: str

    duration: int

    play_url: str
    wmplay_url: str
    """
    The url of the video that includes the watermark.
    """
    hdplay_url: str
    """
    The url of the video that doesn't include the
    watermark.
    """

    size: int
    wm_size: int
    """
    The size of the video that includes the watermark
    and can be downloaded by using the `wmplay_url`.
    """
    hd_size: int
    """
    The size of the video that includes not the
    watermark and can be downloaded by using the
    `hdplay_url`.
    """

    music_url: str
    music_info: TikTokMusicInfo

    play_count: int
    digg_count: int
    comment_count: int
    share_count: int
    download_count: int
    collect_count: int

    create_time: int

    is_ad: bool

    author: TikTokAuthor

    @property
    def url_with_watermark(
        self
    ) -> str:
        """
        The url to download the video that includes the
        watermark.
        """
        return self.wmplay_url
    
    @property
    def url_without_watermark(
        self
    ) -> str:
        """
        The url to download the video that doesn't include
        the watermark.
        """
        return self.hdplay_url

    @classmethod
    def from_dict(
        cls,
        data: dict
    ) -> 'TikTokVideo':
        """
        Provide the `data` field of the JSON response that
        comes when requesting to the endpoint:
        - `https://tikwm.com/api/`

        A valid endpoint is something like this:
        - `https://tikwm.com/api/?url=https%3A%2F%2Fwww.tiktok.com%2F%40numloco1%2Fvideo%2F7632085075613502734&hd=1`
        """
        return cls(
            id = data['id'],
            region = data['region'],
            title = data['title'],

            cover = data['cover'],
            origin_cover = data['origin_cover'],

            duration = data['duration'],

            play_url = data['play'],
            wmplay_url = data['wmplay'],
            hdplay_url = data['hdplay'],

            size = data['size'],
            wm_size = data['wm_size'],
            hd_size = data['hd_size'],

            music_url = data['music'],
            music_info = TikTokMusicInfo(**data['music_info']),

            play_count = data['play_count'],
            digg_count = data['digg_count'],
            # TODO: Map to ints (?)
            comment_count = data['comment_count'],
            share_count = data['share_count'],
            download_count = data['download_count'],
            collect_count = data['collect_count'],

            create_time = data['create_time'],

            # TODO: Map to boolean
            is_ad = data['is_ad'],

            author = TikTokAuthor(**data['author']),
        )
    

"""
You can make a request to an endpoint like the one
above, and obtain the 'data' field and parse it
with the `TikTokVideo.from_dict()`.

Example of information in the 'data' field, extracted
from the video with this url:
- `https://www.tiktok.com/@numloco1/video/7632085075613502734?is_from_webapp=1&sender_device=pc&web_id=7640167403208607240`:

{'id': '7632085075613502734', 'region': 'US', 'title': 'Cómo sacar el url de tiktok: Guía rápida para copiar enlaces 🔗 ¿Tú quieres obtener el link de un video o perfil y no sabes cómo hacerlo? Hazlo ahora Porque TikTok permite copiar la URL fácilmente. Sigue este plan rápido de NumLoco para sacar el URL paso a paso dentro de la app. Soporte y soluciones para apps y redes sociales | NumLoco #NumLoco #TikTokTips #URLTikTok #CompartirTikTok #creatorsearchinsights ', 'content_desc': ['Cómo sacar el url de tiktok: Guía rápida para copiar enlaces 🔗', '¿Tú quieres obtener el link de un video o perfil y no sabes cómo hacerlo? Hazlo ahora Porque TikTok permite copiar la URL fácilmente.', 'Sigue este plan rápido de NumLoco para sacar el URL paso a paso dentro de la app.', 'Soporte y soluciones para apps y redes sociales | NumLoco', '#NumLoco #TikTokTips #URLTikTok #CompartirTikTok', '#creatorsearchinsights '], 'cover': 'https://p16-common-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/o4wAziUN0BArnbewABB4Dd49iA5EJIvIPCYiqa~tplv-tiktokx-cropcenter-q:300:400:q70.jpeg?dr=8596&refresh_token=0570536d&x-expires=1778950800&x-signature=nCAqHXWQJQMXCTILa382UqAkjhk%3D&t=bacd0480&ps=933b5bde&shp=d05b14bd&shcp=1d1a97fc&idc=useast5&biz_tag=tt_video&s=AWEME_DETAIL&sc=cover', 'ai_dynamic_cover': 'https://p16-common-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/o4wAziUN0BArnbewABB4Dd49iA5EJIvIPCYiqa~tplv-tiktokx-origin.image?dr=8606&refresh_token=33cea1dd&x-expires=1778950800&x-signature=QWeb9rT9ryPCkf%2BgEsavbDBsbmM%3D&t=bacd0480&ps=4f5296ae&shp=d05b14bd&shcp=1d1a97fc&idc=useast5&biz_tag=tt_video&s=AWEME_DETAIL&sc=dynamic_cover', 'origin_cover': 'https://p16-common-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/o8BqAHcANcBVAqYPeuef4yNIBTXifgkAQcOfKB~tplv-tiktokx-shrink-aq:360:360:q75.webp?dr=11731&refresh_token=fb4da3a4&x-expires=1778950800&x-signature=AafIbAiEHLB3B0lftbqsCY0hWFM%3D&t=bacd0480&ps=d97f9a4f&shp=d05b14bd&shcp=1d1a97fc&idc=useast5&biz_tag=tt_video&s=AWEME_DETAIL&sc=feed_cover', 'duration': 87, 'play': 'https://v19.tiktokcdn-us.com/7e7f231bafcd48b669d430ebb6410b00/6a07a972/video/tos/useast5/tos-useast5-ve-0068c003-tx/o4SqjTJf1DxEInqtHAEnmykffAMAFFIDQLkCQT/?a=1233&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&&bt=904&ft=kLx3-yt4ZZo0PDbjT43aQ9.SZCpKJE.C~&mime_type=video_mp4&rc=Z2k0aTg0NTNoODNkNGZkNUBpMzkzdnM5cjo8OjMzZzczNEBiMjVhLy81X14xYl8tNTFfYSM1azVjMmRzbWlhLS1kMS9zcw%3D%3D&vvpl=1&l=20260515171539BE56F5C9BB683015CF92&btag=e00090000', 'wmplay': 'https://v19.tiktokcdn-us.com/5d5ce000707b9f8a4ac73abcebbbfe61/6a07a972/video/tos/useast5/tos-useast5-ve-0068c002-tx/ocmynTz3fACzQxDfISDqkfEAAFjFT15ILkEIHQ/?a=1233&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&&bt=829&ft=kLx3-yt4ZZo0PDbjT43aQ9.SZCpKJE.C~&mime_type=video_mp4&rc=aDM5aDQ0ZDhkNGc8Mzo6N0BpMzkzdnM5cjo8OjMzZzczNEBgNDIxMWEyNS4xMzAwNi1gYSM1azVjMmRzbWlhLS1kMS9zcw%3D%3D&vvpl=1&l=20260515171539BE56F5C9BB683015CF92&btag=e00090000', 'hdplay': 'https://v16m-default.tiktokcdn-us.com/9fa085d3e62aade52b1f576891e750e1/6a07a972/video/tos/useast5/tos-useast5-ve-0068c003-tx/o4SqjTJf1DxEInqtHAEnmykffAMAFFIDQLkCQT/?a=0&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&&bt=904&ft=kLMdqyt4ZZo0PDbjT43aQ9qIhKA6JE.C~&mime_type=video_mp4&rc=Z2k0aTg0NTNoODNkNGZkNUBpMzkzdnM5cjo8OjMzZzczNEBiMjVhLy81X14xYl8tNTFfYSM1azVjMmRzbWlhLS1kMS9zcw%3D%3D&vvpl=1&l=20260515171539F1DD5F4F6ADD04164056&btag=e00090000', 'size': 10076248, 'wm_size': 9237829, 'hd_size': 10076248, 'music': 'https://v19-ies-music.tiktokcdn-us.com/0ad5d1e1ad947aab4f21b4fec57d0707/6a108fe9/video/tos/useast5/tos-useast5-v-27dcd7-tx/o0kC1fkEPT7Gie2bgCqTgDeoo9HLVOITAQYYwp/?a=583965&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&&bt=125&ft=kJxKSyt4ZZo0PDbjT43aQ9.SZCpKJE.C~&mime_type=audio_mpeg&rc=ZGVpNzozZDw7Zmg2O2U2OEBpM3hxbnc5cjM8OjMzZzU8NEAxYDQxLmEvXjMxX2BjYmExYSNqZGdrMmRjbmlhLS1kMS9zcw%3D%3D&vvpl=1&l=20260515171539BE56F5C9BB683015CF92&btag=e000d0000&shp=d05b14bd&shcp=-', 'music_info': {'id': '7632085076980894478', 'title': 'original sound - numloco1', 'play': 'https://v19-ies-music.tiktokcdn-us.com/0ad5d1e1ad947aab4f21b4fec57d0707/6a108fe9/video/tos/useast5/tos-useast5-v-27dcd7-tx/o0kC1fkEPT7Gie2bgCqTgDeoo9HLVOITAQYYwp/?a=583965&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&&bt=125&ft=kJxKSyt4ZZo0PDbjT43aQ9.SZCpKJE.C~&mime_type=audio_mpeg&rc=ZGVpNzozZDw7Zmg2O2U2OEBpM3hxbnc5cjM8OjMzZzU8NEAxYDQxLmEvXjMxX2BjYmExYSNqZGdrMmRjbmlhLS1kMS9zcw%3D%3D&vvpl=1&l=20260515171539BE56F5C9BB683015CF92&btag=e000d0000&shp=d05b14bd&shcp=-', 'cover': 'https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/9906c233ef91ccf266e40ffc3bf40ab6~tplv-tiktokx-cropcenter-q:1080:1080:q70.jpeg?dr=8837&idc=useast5&ps=87d6e48a&refresh_token=0d2e88a1&s=AWEME_DETAIL&sc=avatar&shcp=1d1a97fc&shp=d05b14bd&t=223449c4&x-expires=1778950800&x-signature=9lGDlMmWGNac%2B%2FOasnnvtTtexn0%3D', 'author': 'NumLoco♦️', 'original': True, 'duration': 87, 'album': ''}, 'play_count': 5673, 'digg_count': 48, 'comment_count': 8, 'share_count': 8, 'download_count': 5, 'collect_count': 10, 'create_time': 1776983292, 'anchors': None, 'anchors_extras': '', 'is_ad': False, 'commerce_info': {'adv_promotable': False, 'auction_ad_invited': False, 'branded_content_type': 0, 'is_diversion_ad': 0, 'organic_log_extra': '{"req_id":"20260515171539BE56F5C9BB683015CF92"}', 'with_comment_filter_words': False}, 'commercial_video_info': '', 'item_comment_settings': 0, 'mentioned_users': '', 'author': {'id': '7534556192958497805', 'unique_id': 'numloco1', 'nickname': 'NumLoco♦️', 'avatar': 'https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/9906c233ef91ccf266e40ffc3bf40ab6~tplv-tiktokx-cropcenter-q:300:300:q70.jpeg?dr=8834&idc=useast5&ps=87d6e48a&refresh_token=efeb2624&s=AWEME_DETAIL&sc=avatar&shcp=1d1a97fc&shp=d05b14bd&t=223449c4&x-expires=1778950800&x-signature=1yI9FIlLz4mB6Q8QttKk9YDEyvk%3D'}}
"""
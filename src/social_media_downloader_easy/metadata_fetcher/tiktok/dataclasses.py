from dataclasses import dataclass


@dataclass
class TiktokVideoMetadata:
    """
    The metadata that a public Tiktok video has,
    including these fields:
    - `id`
    - `username`
    - `title`
    - `description`
    """

    id: str
    username: str
    title: str
    description: str


@dataclass
class TikTokMetadataEmbed:
    """
    The metadata of a public Tiktik video that has
    been received by using the oembed endpoint,
    including these fields:

    - `description`
    - `author_url`
    - `author_name`
    - `author_username`
    - `thumbnail_width`
    - `thumbnail_height`
    - `thumbnail_url`

    An example of a valid instance:
    {
        'description': 'Cambodia has been so quiet and just wanna assure people it is safe, beautiful and full of the kindest locals you will ever meet \U0001faf6\U0001faf6 will continue to try make content but this holiday season is hitting me hard lol so Im just taking it easy rn hence the puffy eyes #cambodia #kohrong #femaletravel #solotravel #travelcambodia ',
        'author_url': 'https://www.tiktok.com/@laylaloutfi',
        'author_name': 'Layla Loutfi',
        'author_username': 'laylaloutfi',
        'thumbnail_width': 576,
        'thumbnail_height': 1024,
        'thumbnail_url': 'https://p16-common-sign.tiktokcdn.com/tos-no1a-p-0037-no/oo1CFkBtiCUpoxHX3IN4AALC33kIIyCPw0fw8i~tplv-tiktokx-dmt-logom:tos-no1a-i-0068-no/oAER8RECFAR6mPkIE3ZEjEgIDfAfFFA48CAp8Q.image?dr=14573&x-expires=1787814000&x-signature=C0l%2FSxubW%2BNqD5w97fWo2qB4IRI%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=my'
    }

    The embed endpoint is this one:
    - https://www.tiktok.com/oembed?url={URL_TIKTOK}
    """

    description: str
    """
    The description of the video, which could be
    also the title.
    """
    author_url: str
    """
    The url to visit the author's profile page.
    """
    author_name: str
    """
    The real name of the author that is displayed
    while watching the video.
    """
    author_username: str # author_unique_id
    """
    The unique username, including not the @.
    """
    thumbnail_width: int
    thumbnail_height: int
    thumbnail_url: str
    """
    The url to obtain the thumbnail image directly.
    """


    @property
    def as_dict(
        self
    ) -> dict:
        """
        Get the metadata as a dict like this,
        perfect to serialize it and store in
        a database.
        ```
        {
            'description': self.description,
            'author_url': self.author_url,
            'author_name': self.author_name,
            'author_username': self.author_username,
            'thumbnail_width': self.thumbnail_width,
            'thumbnail_height': self.thumbnail_height,
            'thumbnail_url': self.thumbnail_url
        }
        ```
        """
        return {
            'description': self.description,
            'author_url': self.author_url,
            'author_name': self.author_name,
            'author_username': self.author_username,
            'thumbnail_width': self.thumbnail_width,
            'thumbnail_height': self.thumbnail_height,
            'thumbnail_url': self.thumbnail_url
        }
        

    @classmethod
    def from_dict(
        cls,
        data: dict
    ) -> 'TikTokMetadataEmbed':
        return cls(
            description = data['title'],
            author_url = data['author_url'],
            author_name = data['author_name'],
            author_username = data['author_unique_id'],
            thumbnail_width = data['thumbnail_width'],
            thumbnail_height = data['thumbnail_height'],
            thumbnail_url = data['thumbnail_url'],
        )



"""
The embed endpoint is this one:
- https://www.tiktok.com/oembed?url=https%3A%2F%2Fvm.tiktok.com%2FZN8eRVqJa

And returns a response like this:
{
    "version": "1.0",
    "type": "video",
    "title": "Cambodia has been so quiet and just wanna assure people it is safe, beautiful and full of the kindest locals you will ever meet 🫶🫶 will continue to try make content but this holiday season is hitting me hard lol so I’m just taking it easy rn hence the puffy eyes #cambodia #kohrong #femaletravel #solotravel #travelcambodia ",
    "author_url": "https://www.tiktok.com/@laylaloutfi",
    "author_name": "Layla Loutfi",
    "width": "100%",
    "height": "100%",
    "html": "<blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@laylaloutfi/video/7586250089434221846\" data-video-id=\"7586250089434221846\" data-embed-from=\"oembed\" style=\"max-width:605px; min-width:325px;\"> <section> <a target=\"_blank\" title=\"@laylaloutfi\" href=\"https://www.tiktok.com/@laylaloutfi?refer=embed\">@laylaloutfi</a> <p>Cambodia has been so quiet and just wanna assure people it is safe, beautiful and full of the kindest locals you will ever meet 🫶🫶 will continue to try make content but this holiday season is hitting me hard lol so I’m just taking it easy rn hence the puffy eyes <a title=\"cambodia\" target=\"_blank\" href=\"https://www.tiktok.com/tag/cambodia?refer=embed\">#cambodia</a> <a title=\"kohrong\" target=\"_blank\" href=\"https://www.tiktok.com/tag/kohrong?refer=embed\">#kohrong</a> <a title=\"femaletravel\" target=\"_blank\" href=\"https://www.tiktok.com/tag/femaletravel?refer=embed\">#femaletravel</a> <a title=\"solotravel\" target=\"_blank\" href=\"https://www.tiktok.com/tag/solotravel?refer=embed\">#solotravel</a> <a title=\"travelcambodia\" target=\"_blank\" href=\"https://www.tiktok.com/tag/travelcambodia?refer=embed\">#travelcambodia</a> </p> <a target=\"_blank\" title=\"♬ original sound - Layla Loutfi\" href=\"https://www.tiktok.com/music/original-sound-7586250090089483030?refer=embed\">♬ original sound - Layla Loutfi</a> </section> </blockquote> <script async src=\"https://www.tiktok.com/embed.js\"></script>",
    "thumbnail_width": 576,
    "thumbnail_height": 1024,
    "thumbnail_url": "https://p16-common-sign.tiktokcdn.com/tos-no1a-p-0037-no/oo1CFkBtiCUpoxHX3IN4AALC33kIIyCPw0fw8i~tplv-tiktokx-dmt-logom:tos-no1a-i-0068-no/oAER8RECFAR6mPkIE3ZEjEgIDfAfFFA48CAp8Q.image?dr=14573&x-expires=1786856400&x-signature=P60HbKD9HsEsdxJqaIVD014cVT4%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=my",
    "provider_url": "https://www.tiktok.com",
    "provider_name": "TikTok",
    "author_unique_id": "laylaloutfi",
    "embed_product_id": "7586250089434221846",
    "embed_type": "video"
}
"""
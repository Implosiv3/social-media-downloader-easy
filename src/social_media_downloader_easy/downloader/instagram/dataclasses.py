from dataclasses import dataclass


@dataclass
class InstagramUrl:
    """
    Class to hold the information about a
    InstagramUrl.
    """

    def __init__(
        self,
        id: str,
        url: str
    ):
        self.id: str = id
        """
        The id of the video.
        """
        self.url: str = url
        """
        The short Instagram url of that video.
        """
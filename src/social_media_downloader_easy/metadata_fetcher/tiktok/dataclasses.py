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
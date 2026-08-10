def clean_url(
    url: str
) -> str:
    """
    Clean the `url` provided by removing any
    additional parameter that is after a
    question mark sign.
    """
    return (
        url.split('?')[0]
        if '?' in url else
        url
    )
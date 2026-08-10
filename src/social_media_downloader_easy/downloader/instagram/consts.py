DOWNLOADGRAM_DOWNLOAD_INSTAGRAM_VIDEO_WEBSITE_URL = 'https://downloadgram.org/video-downloader.php'
FASTVIDEOSAVE_DOWNLOAD_INSTAGRAM_VIDEO_WEBSITE_URL = 'https://fastvideosave.net/'
IGMEDIA_DOWNLOAD_INSTAGRAM_VIDEO_HEADERS = {
    # TODO: This x-hmac-signature looks that we have to renew it
    'x-hmac-signature': '6d4fd85af287b6d389ac1ece7dfa4c9b45d760fa6c2b5dabf0b4076ff6a6d9bb',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.ig.media/',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'x-timestamp': '1779082613645',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
}
"""
The headers of the `https://www.ig.media/` platform
that is meant to download Instagram videos.
"""
IGMEDIA_DOWNLOAD_INSTAGRAM_VIDEO_ENDPOINT_URL = 'https://api.ig.media/api/instagram-media'
"""
Endpoint to get the download url of an Instagram
video, based on an endpoint that is not strictly
secured.
"""
IGMEDIA_DOWNLOAD_INSTAGRAM_VIDEO_HMAC_SECRET = '38439a9d35050fd482cc114a8c455d239e666c87f8d58912bb15fa67f35866ca'
"""
This HMAC Secret was found hardcoded in:
- https://www.ig.media/assets/chunks/chunk-BdVi1FDv.js
"""


# Social Media Downloader, but made easy

A way to __download videos from Facebook, Tiktok, Instagram, and more__ social media platforms.

# Functionality
__Download videos__ from social media instantly by pasting the link.

# Usage
Here you have __some examples__:

1. Download from Instagram:
```
from social_media_downloader_easy.downloader import SocialMediaDownloader

async with SocialMediaDownloader(do_follow_redirects = True) as social_media_downloader:
    output_filename = f'test_files/instagram_reel.mp4'

    instagram_video_downloaded = await social_media_downloader.instagram.download_video(
        url = 'https://www.instagram.com/reel/DHtsmGHTOn4/',
        output_filename = output_filename
    )

    assert instagram_video_downloaded.filename == output_filename
```

Check the `tests` section to see more examples.
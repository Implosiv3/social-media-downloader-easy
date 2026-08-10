"""
Old code I bring here just in case to have
alternatives.
"""

# TODO: Now we have the public 'web_scraper' library
# @requires_dependency('yta_web_scraper', 'yta_file_downloader', 'yta_web_scraper')
# async def download_instagram(
#     self,
#     url: str,
#     output_filename: str
# ) -> FileResource:
#     """
#     *Optional dependency required: `yta_web_scraper`*

#     Download an Instagram video from the `url`
#     provided and save it to the `output_filename`
#     if given.

#     This method will scrape a website platform to
#     obtain the video.

#     This method returns a `FileResource` instance.
#     """
#     from yta_web_scraper.chrome import ChromeScraper, By
    
#     # This method is based on the external website below, so
#     # it could stop working when that website is off.
#     # TODO: Try to make alternatives with other web pages.
    
#     scraper = ChromeScraper.init()
#     scraper.go_to_web_and_wait_until_loaded(DOWNLOADGRAM_DOWNLOAD_INSTAGRAM_VIDEO_WEBSITE_URL)

#     # We need to place the url in the input and press enter
#     url_input = scraper.find_element_by_id_waiting('url')
#     url_input.send_keys(url)

#     """
#     I need to remove the elements related to advertisement
#     because they are intercepting my clicks. Those ones 
#     which id starts with 'aswift'.
#     """
#     scraper.execute_script(
#         """
#         for (const element of document.querySelectorAll('[id*="aswift"]')) {
#             element.remove();
#         }
#         """
#     )
    
#     submit_button = scraper.find_element_by_id_waiting('submit')
#     submit_button.click()

#     # We need to wait until video is shown
#     video_element = scraper.find_element_by_element_type_waiting('video')
#     video_source_element = video_element.find_element(By.TAG_NAME, 'source')
#     video_source_url = video_source_element.get_attribute('src')

#     # This just downloads the thumbnail but, for what (?)
#     # thumbnail_image_url = video_element.get_attribute('poster')
#     # download_image(thumbnail_image_url, 'test_instagram_image.png')

#     with self.follow_redirects(True):
#         file_resource = await self._get_file(
#             url = video_source_url,
#             output_filename = Output.get_filename(
#                 filename = output_filename,
#                 file_extension = VideoFileExtension
#             )
#         )

#         file_resource.parsing_method = FileParsingMethod.MOVIEPY_VIDEO
#         file_resource.source_url = video_source_url

#         return file_resource 

#     """
#     TODO: Previously we were storing the video as
#     the content itself. Remove this below when
#     confirmed that is ok.
#     """
#     # if output_filename is False:
#     #     return BytesIO(get_file(video_source_url, None))
    
#     # output_filename = Output.get_filename(output_filename, VideoFileExtension)
#     # video = get_file(video_source_url, output_filename)

#     # return FileReturned(
#     #     # TODO: Make this work with videos in memory also
#     #     # but, by now, as file because of 'moviepy'
#     #     content = video,
#     #     filename = None,
#     #     output_filename = output_filename,
#     #     type = None,
#     #     is_parsed = False,
#     #     # TODO: Write the code that, when using this
#     #     # FileParsingMethod, uses the 'output_filename'
#     #     # as the 'filename' to read it
#     #     parsing_method = FileParsingMethod.MOVIEPY_VIDEO,
#     #     extra_args = None
#     # )


# @requires_dependency('yta_web_scraper', 'yta_file_downloader', 'yta_web_scraper')
# async def download_instagram_2(
#     self,
#     url: str,
#     output_filename: str
# ) -> FileResource:
#     """
#     *Optional dependency required: `yta_web_scraper`*

#     Download an Instagram video from the `url`
#     provided and save it to the `output_filename`
#     if given.

#     This method will scrape a website platform to
#     obtain the video.

#     This method returns a `FileResource` instance.
#     """
#     from yta_web_scraper.chrome import ChromeScraper, Keys
    
#     scraper = ChromeScraper.init()
#     scraper.go_to_web_and_wait_until_loaded(FASTVIDEOSAVE_DOWNLOAD_INSTAGRAM_VIDEO_WEBSITE_URL)

#     """
#     This webpage is accepting only links that are pasted,
#     if you start writing it will detect a valid link and
#     send it before you can finish writing it full
#     """
#     scraper.add_to_clipboard(url)
#     scraper.find_element_by_custom_tag_waiting('input', 'name', 'url')

#     # TODO: Maybe we can improve this to use elements instead
#     scraper.press_key_x_times(
#         key = Keys.TAB,
#         times = 5
#     )
#     scraper.press_ctrl_v()

#     video_download_button = scraper.find_element_by_custom_tag_waiting('a', 'aria-label', 'Download Video')
#     video_source_url = video_download_button.get_attribute('href')

#     with self.follow_redirects(True):
#         file_resource = await self._get_file(
#             url = video_source_url,
#             output_filename = Output.get_filename(
#                 filename = output_filename,
#                 file_extension = VideoFileExtension
#             )
#         )

#         file_resource.parsing_method = FileParsingMethod.MOVIEPY_VIDEO
#         file_resource.source_url = video_source_url

#         return file_resource 
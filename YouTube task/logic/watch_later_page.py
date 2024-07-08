from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class WatchLaterPage(BasePageApp):
    WATCH_LATER_VIDEOS_LIST = '//h3[@class ="style-scope ytd-playlist-video-renderer"]'
    LATEST_WATCH_LATER_VIDEO = '(//h3[@class ="style-scope ytd-playlist-video-renderer"])[1]'

    def __init__(self, driver):
        super().__init__(driver)
        self._watch_later_videos_list = self._driver.find_elements(By.XPATH, self.WATCH_LATER_VIDEOS_LIST)
        self._latest_watch_later_video = self._driver.find_element(By.XPATH, self.LATEST_WATCH_LATER_VIDEO)

    def get_watch_later_videos(self):
        """Returns a list of titles of videos in the Watch Later playlist."""
        return [video.text for video in self._watch_later_videos_list]

    def get_latest_watch_later_video(self):
        return self._latest_watch_later_video.text

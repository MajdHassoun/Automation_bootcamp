from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class LikedVideosPage(BasePageApp):
    LIKED_VIDEOS_LIST = '//h3[@class ="style-scope ytd-playlist-video-renderer"]'
    RECENT_LIKED_VIDEO = '(//h3[@class ="style-scope ytd-playlist-video-renderer"])[1]'

    def __init__(self, driver):
        super().__init__(driver)
        self._liked_videos_list = self._driver.find_elements(By.XPATH, self.LIKED_VIDEOS_LIST)
        self._recent_liked_video = self._driver.find_element(By.XPATH, self.RECENT_LIKED_VIDEO)

    def get_liked_videos(self):
        """Returns a list of titles of liked videos."""
        return [video.text for video in self._liked_videos_list]

    def get_recent_liked_video(self):
        return self._recent_liked_video.text

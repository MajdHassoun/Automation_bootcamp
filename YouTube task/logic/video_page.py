from selenium.webdriver.common.by import By

from infra.base_page import BasePage


# like,sub,save,channel name, video name
class VideoPage(BasePage):
    LIKE_BUTTON = '(//button[@title = "I like this"])[1]'
    UNLIKE_BUTTON = '(//button[@title = "Unlike"])[1]'
    SUBSCRIBE_BUTTON = '//div[@id ="above-the-fold"]' \
                       '//button[@class =' \
                       ' "yt-spec-button-shape-next yt-spec-button-shape-next--filled' \
                       ' yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m"]'
    THREE_POINTS_BUTTON = '(//button[@aria-label="More actions"]' \
                          '//div[@class = "yt-spec-touch-feedback-shape__stroke"])[1]'
    SAVE_BUTTON = '//yt-formatted-string[text() = "Save"]'
    WATCH_LATER_CHECKBOX = '(//tp-yt-paper-checkbox[@id= "checkbox"])[1]'
    SAVED_TO_WATCH_LATER_MESSAGE = '(//div[@id = "text-container"]//' \
                                   'yt-formatted-string[text() = "Saved to Watch Later"])[1]'
    CHANNEL_NAME = '(//ytd-channel-name[@id = "channel-name"]' \
                   '//a[@class = "yt-simple-endpoint style-scope yt-formatted-string"])[4]'
    VIDEO_NAME = '//h1[@class = "style-scope ytd-watch-metadata"]' \
                 '//yt-formatted-string[@class = "style-scope ytd-watch-metadata"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._like_button = self._driver.find_element(By.XPATH, self.LIKE_BUTTON)
        self._unlike_button = self._driver.find_element(By.XPATH, self.UNLIKE_BUTTON)
        self._subscribe_button = self._driver.find_element(By.XPATH, self.SUBSCRIBE_BUTTON)
        self._three_points_button = self._driver.find_element(By.XPATH, self.THREE_POINTS_BUTTON)
        self._save_button = self._driver.find_element(By.XPATH, self.SAVE_BUTTON)
        self._watch_later_checkbox = self._driver.find_element(By.XPATH, self.WATCH_LATER_CHECKBOX)
        self._saved_to_watch_later_message = self._driver.find_element(By.XPATH, self.SAVED_TO_WATCH_LATER_MESSAGE)
        self._channel_name = self._driver.find_element(By.XPATH, self.CHANNEL_NAME)
        self._video_name = self._driver.find_element(By.XPATH, self.VIDEO_NAME)

    def like_video(self):
        self._like_button.click()

    def unlike_video(self):
        self._unlike_button.click()

    def subscribe_channel(self):
        self._subscribe_button.click()

    def open_more_actions(self):
        self._three_points_button.click()

    def save_button(self):
        self._save_button.click()

    def add_to_watch_later(self):
        self._watch_later_checkbox.click()

    def is_saved_to_watch_later(self):
        return self._saved_to_watch_later_message.is_displayed()

    def get_channel_name(self):
        return self._channel_name.text

    def get_video_name(self):
        return self._video_name.text

    def save_to_watch_later_flow(self):
        self.open_more_actions()
        self.save_button()
        self.add_to_watch_later()

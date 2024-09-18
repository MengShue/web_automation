from .base_page import BasePage
from selenium.webdriver.common.by import By
from config import Config
from selenium.common import TimeoutException


class VideoStreamPage(BasePage):

    share_btn = (By.XPATH, '//*[text()="Share this video"]')
    audio_copyright_muted_pop = (By.XPATH, '//*[text()="Audio for portions of this video has been muted as it appears'
                                           ' to contain copyrighted content owned or controlled by a third party."]')
    audio_copyright_muted_pop_close = (By.XPATH, '//*[@aria-label="Dismiss muted audio notice"]')

    def __init__(self, driver, config: Config, env=None):
        super().__init__(driver, config, env)

    def is_loaded(self):
        self.is_all_tabs_loaded()
        self.action.is_element_visible(self.share_btn)

    def is_audio_muted_pop_shown(self):
        try:
            self.action.is_element_visible(self.audio_copyright_muted_pop)
            return True
        except TimeoutException:
            return False

    def click_close_audio_muted_pop(self):
        self.action.is_element_visible(self.audio_copyright_muted_pop_close)
        self.action.click_element(self.audio_copyright_muted_pop_close)

    def is_video_loaded(self):
        self.action.wait_for_condition_complete(self.is_document_ready, 20)

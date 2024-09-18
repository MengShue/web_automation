from selenium.common import TimeoutException
from .base_page import BasePage
from selenium.webdriver.common.by import By
from config import Config


class SearchResultPage(BasePage):

    search_bar = (By.XPATH, '//*[@type="search"]')
    back_btn = (By.XPATH, '//*[@aria-label="Back"]')
    top_tab = (By.XPATH, '//*[text()="Top"]')
    channels_tab = (By.XPATH, '//*[text()="Channels"]')
    categories_tab = (By.XPATH, '//*[text()="Categories"]')
    videos_tab = (By.XPATH, '//*[text()="Videos"]')

    def __init__(self, driver, config: Config, env=None):
        super().__init__(driver, config, env)

    def is_loaded(self):
        self.action.is_element_visible(self.search_bar)
        self.action.is_element_visible(self.back_btn)
        self.action.is_element_visible(self.top_tab)
        self.action.is_element_visible(self.channels_tab)
        self.action.is_element_visible(self.categories_tab)
        self.action.is_element_visible(self.videos_tab)

    def check_video_section_exist(self):
         videos_section = (By.XPATH,'//*[text() = "VIDEOS"]')
         try:
            self.action.is_element_visible(videos_section)
            return True
         except TimeoutException:
            return False

    def click_video_by_index(self, index):
        videos_list = (By.XPATH, f"(//*[contains(@href,\"/video\")])[{str(index)}]")
        self.action.is_element_visible(videos_list)
        self.action.click_element(videos_list)

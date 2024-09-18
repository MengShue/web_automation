from .base_page import BasePage
from selenium.webdriver.common.by import By
from config import Config


class SearchPage(BasePage):

    search_bar = (By.XPATH, '//*[@placeholder="Search..."]')
    back_btn = (By.XPATH, '//*[@aria-label="Back"]')

    def __init__(self, driver, config: Config, env=None):
        super().__init__(driver, config, env)

    def is_loaded(self):
        self.action.is_element_visible(self.search_bar)
        self.action.is_element_visible(self.back_btn)

    def click_search_button(self):
        self.action.click_element(self.search_bar)

    def enter_search_text(self, text):
        self.action.send_keys_to_element(self.search_bar, text)

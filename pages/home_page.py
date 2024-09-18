from .base_page import BasePage
from selenium.webdriver.common.by import By
from config import Config


class HomePage(BasePage):

    title = (By.XPATH, '//*[title="Twitch"]')
    live_section = (By.XPATH, '//*[text() = "Live channels"]')
    section_suffix_str = (By.XPATH, '(//*[text()=" we think you’ll like"])[1]')
    category_section = (By.XPATH, '//*[text() = "Categories"]')

    def __init__(self, driver, config: Config, env=None):
        super().__init__(driver, config, env)

    def load(self):
        base_url = self.config.get_base_url(self.env)
        self.driver.get(base_url)

    def is_loaded(self):
        self.action.is_element_present(self.title)
        self.is_all_tabs_loaded()
        self.action.is_element_visible(self.live_section)
        self.action.is_element_visible(self.section_suffix_str)

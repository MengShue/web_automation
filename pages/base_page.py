from config import Config
from actions.base_action import BaseAction
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os
from selenium.webdriver.common.by import By


class BasePage:

    go_homepage_btn = (By.XPATH, '//*[@aria-label="Go to the Twitch home page"]')
    go_games_btn = (By.XPATH, '//*[@aria-label="Go to all games page"]')
    top_menu_btn = (By.XPATH, '//*[@aria-label="Show top navigation menu"]')
    search_btn = (By.XPATH, '//*[@href="/search"]')
    user_menu_btn = (By.XPATH, '//*[@aria-label="Show user menu"]')

    def __init__(self, driver, config: Config, env=None):
        self.driver = driver
        self.config = config
        self.env = env or self.config.get_env()
        self.action = BaseAction(self.driver, timeout=config.get_explicitly_timeout())

    def is_all_tabs_loaded(self):
        self.action.is_element_visible(self.go_homepage_btn)
        self.action.is_element_visible(self.go_games_btn)
        self.action.is_element_visible(self.top_menu_btn)
        self.action.is_element_visible(self.search_btn)
        self.action.is_element_visible(self.user_menu_btn)

    def click_search_button(self):
        self.action.click_element(self.search_btn)

    def scroll(self):
        self.action.scroll()
        self.wait(1)

    def enter(self):
        self.action.press_key(Keys.RETURN)

    def wait(self,seconds):
        self.action.sleep(seconds)

    def is_document_ready(self):
        if self.driver.execute_script("document.readyState;") == 'complete':
            return True
        else:
            return False

    def save_screenshot(self):
        timestamp = time.time()
        tims_string = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d-%H:%M:%S')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.action.screenshot(f"{dir_path}/../screenshot/{tims_string}.png")

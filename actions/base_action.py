import time
from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BaseAction:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.actions = ActionChains(self.driver)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys_to_element(self, locator, keys):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(keys)

    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def scroll_into_view(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def hover_over_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).perform()

    def press_key(self, key):
        self.actions.send_keys(key).perform()

    def is_element_present(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def is_element_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)

    def sleep(self, sec):
        sleep(sec)

    def wait_for_condition_complete(self,condition, timeout):
        start_time = int(time.time())
        while True:
            if condition:
                return True
            else:
                time.sleep(0.5)
            if time.time() - start_time > timeout:
                raise TimeoutException

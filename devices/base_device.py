from selenium.webdriver.chrome.options import Options

class BaseDevice:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--incognito")
        self.options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.options.headless = True

    def get_options(self):
        return self.options
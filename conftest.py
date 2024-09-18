import pytest
from selenium import webdriver
from devices.base_device import BaseDevice
from devices.iphone_x import iPhoneXDevice
from config import Config

def pytest_addoption(parser):
    parser.addoption(
        "--device", action="store", default="", help="device type,ex. iPhoneX"
    )
    parser.addoption(
        "--env", action="store", default=None, help="testing env, ex. development,production"
    )

@pytest.fixture(scope="session")
def config():
    return Config()

@pytest.fixture(scope="session")
def driver(request, config):
    device_type = request.config.getoption("--device")
    env = request.config.getoption("--env") or config.config.get("DEFAULT_ENV", "production")

    if device_type == 'Desktop':
        device = BaseDevice()
    else:
        device = iPhoneXDevice()  # default Device = iPhone

    chrome_options = device.get_options()
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

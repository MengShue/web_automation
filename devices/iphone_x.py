from .base_device import BaseDevice

class iPhoneXDevice(BaseDevice):

    def __init__(self):
        super().__init__()
        mobile_emulation = { "deviceName": "iPhone X" }
        self.options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.options.add_argument("--window-size=375,812")
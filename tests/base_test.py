import pytest


class BaseTest:


    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver, config):
        """自動執行的設置和拆卸方法"""
        self.driver = driver
        self.environment = config.get_env()
        self.config = config
        self.setup_func()
        yield
        self.teardown_func()

    def setup_func(self):
        print("test setup")
        pass

    def teardown_func(self):
        print("test teardown")
        pass

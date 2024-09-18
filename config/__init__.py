import yaml
import os


class Config:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_file = f"{dir_path}/config.yaml"
        self.config_file = config_file
        self._load_config()

    def _load_config(self):
        with open(self.config_file, "r") as file:
            self.config = yaml.safe_load(file)

    def get_env(self):
        env = self.config.get("DEFAULT_ENV", "production")
        return env

    def get_base_url(self, env=None):
        env = env or self.get_env()
        return self.config["BASE_URLS"].get(env, self.config["BASE_URLS"]["production"])

    def get_implicitly_timeout(self):
        return self.config.get("IMPLICITLY_TIMEOUT", 10)

    def get_explicitly_timeout(self):
        return self.config.get("EXPLICITLY_TIMEOUT", 10)

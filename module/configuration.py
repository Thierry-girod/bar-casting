import os
import yaml
from pathlib import Path
import collections

LOCAL_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
PROJECT_ROOT = os.path.abspath(os.path.join(LOCAL_DIR, os.path.pardir))


def deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            d[k] = deep_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


class Configuration:
    def __init__(self):
        self.config = {}

        # Global config file
        with open(os.path.join(PROJECT_ROOT, "config", "config.yml"), 'r') as stream:
            self.config = yaml.load(stream)

        # local config file
        config_local_file = Path(os.path.join(PROJECT_ROOT, "config", "config_local.yml"))
        if config_local_file.is_file():
            with open(os.path.join(PROJECT_ROOT, "config", "config_local.yml"), 'r') as stream:
                config_local = yaml.load(stream)
                # All configuration with local override global
                deep_update(self.config, config_local)


_configuration = Configuration()


def get_config():
    return _configuration.config

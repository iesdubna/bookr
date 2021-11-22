import os.path
import yaml

CONF = None


def init(config_file):
    global CONF
    with open(config_file) as f:
        CONF = yaml.safe_load(f)


def datapath(relative_path):
    return os.path.join(CONF["datadir"], relative_path)

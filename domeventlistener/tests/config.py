import json
import os


CONFIG_PATH = 'domeventlistener/tests/config.json'
config = {}


if os.path.isfile(CONFIG_PATH):
    with open(CONFIG_PATH) as _file:
        config = json.loads(_file.read())
    _file.close()

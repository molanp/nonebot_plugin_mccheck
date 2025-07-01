import os

import ujson

from .config import config as plugin_config


def readInfo(file: str) -> dict:
    with open(
        os.path.join(os.path.dirname(__file__), file), encoding="utf-8"
    ) as f:
        return ujson.loads((f.read()).strip())


message_type = plugin_config.type
lang = plugin_config.language
lang_data = readInfo("language.json")
VERSION = "0.2.0"

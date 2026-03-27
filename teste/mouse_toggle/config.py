# config.py - Salva e carrega a configuracao do app em JSON

import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

DEFAULT_CONFIG = {
    "hotkey": "F9",
}


def load_config():
    """Carrega a config do arquivo. Se nao existir, retorna o padrao."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return DEFAULT_CONFIG.copy()


def save_config(config):
    """Salva a config no arquivo JSON."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

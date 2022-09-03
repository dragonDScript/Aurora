from os import path
from pathlib import Path
import json
from PySide6.QtWidgets import QWidget

config_path = path.join(str(Path.home()), ".aurora.json")
default_settings = {}
settings_cache = {}

def create_file_if_not_existent():
    with open(config_path, 'w+') as f:
        f.write(json.dumps(default_settings))
        f.close()

def cache_settings_get():
    with open(config_path, 'r') as f:
        global settings_cache
        settings_cache = json.loads(f.read())
        f.close()

def dump_cached_settings():
    with open(config_path, 'w') as f:
        global settings_cache
        f.write(json.dumps(settings_cache))
        f.close()

create_file_if_not_existent()
cache_settings_get()

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setFixedSize(512, 256)

from os import path
from pathlib import Path
import json
from PySide6.QtWidgets import QTabWidget, QWidget, QFormLayout

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

class SettingsWindow(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setFixedSize(412, 512)
        self.general_widget = QWidget()
        self.general_layout = QFormLayout(self.general_widget)
        self.general_layout
        self.addTab(self.general_widget, "General")
        self.addTab(QWidget(), "Third-party")
        self.addTab(QWidget(), "Credits")
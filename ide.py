import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QToolButton

from fexplorer import FileExplorer
from tabs import Tabs

class Window(QWidget):
    # Setups the necessary layouts for the GUI
    def setup_layouts(self) -> None:
        self.cont_layout = QHBoxLayout()
        self.setLayout(self.cont_layout)
        self.cont_editor = QWidget()
        self.cont_editor_layout = QVBoxLayout()
        self.cont_editor.setLayout(self.cont_editor_layout)

        self.qa = QWidget()
        self.qa_layout = QHBoxLayout()
        self.qa.setLayout(self.qa_layout)

    def render(self) -> None:
        self.setup_layouts()

        self.tabs = Tabs()

        self.save_btn = QToolButton(self.tabs)
        self.save_btn.setFixedSize(32, 32)
        self.save_btn.setIcon(QIcon("save_black_24dp.png"))
        self.save_btn.clicked.connect(self.tabs.overwrite_tab_file_contents)

        self.open_folder_btn = QToolButton(self.tabs)
        self.open_folder_btn.setFixedSize(32, 32)
        self.open_folder_btn.setIcon(QIcon("folder_open_black_24dp.png"))
        self.open_folder_btn.clicked.connect(self.tabs.ui_open_folder)

        self.settings_btn = QToolButton(self.tabs)
        self.settings_btn.setFixedSize(32, 32)
        self.settings_btn.setIcon(QIcon("settings_black_24dp.png"))

        self.about_btn = QToolButton(self.tabs)
        self.about_btn.clicked.connect(self.tabs.show_welcome_tab)
        self.about_btn.setFixedSize(32, 32)
        self.about_btn.setIcon(QIcon("info_black_24dp.png"))

        self.file_explorer = FileExplorer()
        self.file_explorer.clicked.connect(self.tabs.add_file_tab_signal)
        self.cont_layout.addWidget(self.file_explorer)
        self.cont_layout.addWidget(self.cont_editor)
        
        self.qa_layout.addWidget(self.open_folder_btn)
        self.qa_layout.addWidget(self.save_btn)
        self.qa_layout.addWidget(self.settings_btn)
        self.qa_layout.addWidget(self.about_btn)
        self.qa_layout.addStretch()

        self.cont_editor_layout.addWidget(self.qa)
        self.cont_editor_layout.addWidget(self.tabs)

    def post_render(self):
        # render folder if there is an argument or fallback to do nothing
        try:
            if sys.argv[1] != None:
                self.file_explorer.render_folder(sys.argv[1])
        except:
            return

    window_minimum_size = (840, 720)
    window_default_size = (1080, 720)
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Aurora")
        self.setMinimumSize(self.window_minimum_size[0], self.window_minimum_size[1])
        self.resize(self.window_default_size[0], self.window_default_size[1])

        self.render()
        self.post_render()

def main():
    app = QApplication()
    win = Window()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

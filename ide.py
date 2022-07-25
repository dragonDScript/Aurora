import sys
from os import path

from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QTreeView, QToolButton, QPlainTextEdit, QFileSystemModel, QFileDialog
from PySide6.QtCore import QDir

class Window(QWidget):
    def setup_layouts(self) -> None:
        self.cont_layout = QHBoxLayout()
        self.setLayout(self.cont_layout)
        self.cont_editor = QWidget()
        self.cont_editor_layout = QVBoxLayout()
        self.cont_editor.setLayout(self.cont_editor_layout)

        self.qa = QWidget()
        self.qa_layout = QHBoxLayout()
        self.qa.setLayout(self.qa_layout)
    # From working directory
    def add_file_tab(self, path_file):
        self.tabs.addTab(QPlainTextEdit(), path.basename(path.normpath(path_file)))
    def set_folder(self, folder_path):
        model = QFileSystemModel(self.file_explorer)
        model.index = model.setRootPath(folder_path)
        self.file_explorer.setModel(model)
    def ui_open_folder(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.set_folder(folderpath)
    def render(self) -> None:
        self.setup_layouts()

        self.tabs = QTabWidget()
        self.save_btn = QToolButton(self.tabs)
        self.save_btn.setFixedSize(32, 32)
        self.save_btn.setIcon(QIcon("save_black_24dp.png"))
        self.open_folder_btn = QToolButton(self.tabs)
        self.open_folder_btn.setFixedSize(32, 32)
        self.open_folder_btn.setIcon(QIcon("folder_open_black_24dp.png"))
        self.open_folder_btn.clicked.connect(self.ui_open_folder)
        self.settings_btn = QToolButton(self.tabs)
        self.settings_btn.setFixedSize(32, 32)
        self.settings_btn.setIcon(QIcon("settings_black_24dp.png"))
        self.file_explorer = QTreeView()
        self.file_explorer.setFixedWidth(256)

        self.cont_layout.addWidget(self.file_explorer)
        self.cont_layout.addWidget(self.cont_editor)
        
        self.qa_layout.addWidget(self.open_folder_btn)
        self.qa_layout.addWidget(self.save_btn)
        self.qa_layout.addWidget(self.settings_btn)
        self.qa_layout.addStretch()

        self.cont_editor_layout.addWidget(self.qa)
        self.cont_editor_layout.addWidget(self.tabs)

        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Nadie")
        self.setMinimumSize(840, 720)
        self.resize(1080, 720)

        self.render()

def main():
    app = QApplication()
    win = Window()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

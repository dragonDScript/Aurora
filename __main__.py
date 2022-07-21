import sys
from os import path

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QTreeView, QToolButton, QPushButton, QPlainTextEdit, QFileSystemModel, QFileDialog
from PySide6.QtCore import QModelIndex

class Window(QWidget):
    def setup_layouts(self) -> None:
        self.cont_layout = QHBoxLayout()
        self.setLayout(self.cont_layout)

        self.cont_editor = QWidget()
        self.cont_editor_layout = QVBoxLayout()
        self.cont_editor.setLayout(self.cont_editor_layout)

        self.qa = QWidget()
        self.qa_layout = QHBoxLayout()
        self.qa.setFixedHeight(64)
        self.qa.setLayout(self.qa_layout)
    # From working directory
    def add_file_tab(self, path_file):
        self.tabs.addTab(QPlainTextEdit(), path.basename(path.normpath(path_file)))
    def set_folder(self, folder_path):
        model = QFileSystemModel()
        model.setRootPath(folder_path)
        index = QModelIndex()
        self.file_explorer.setRootIndex(index)
        self.file_explorer.setModel(model)
    def ui_open_folder(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.set_folder(folderpath)
    def render(self) -> None:
        self.setup_layouts()

        self.tabs = QTabWidget()
        self.save_btn = QPushButton("Save")
        self.open_folder_btn = QPushButton("Open folder")
        self.open_folder_btn.clicked.connect(self.ui_open_folder)
        self.settings_btn = QPushButton("Settings")
        self.file_explorer = QTreeView()
        self.file_explorer.setFixedWidth(256)

        self.cont_layout.addWidget(self.file_explorer)
        self.cont_layout.addWidget(self.cont_editor)
        
        self.qa_layout.addWidget(self.open_folder_btn)
        self.qa_layout.addWidget(self.save_btn)
        self.qa_layout.addWidget(self.settings_btn)

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

import sys
from os import path

from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QTreeView, QToolButton, QPlainTextEdit, QFileSystemModel, QFileDialog, QTextEdit
from PySide6.QtCore import QDir

class FileExplorer(QTreeView):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedWidth(256)
    def render_folder(self, folder_path):
        self._model = QFileSystemModel(self)
        self.setModel(self._model)
        self.setRootIndex(self._model.setRootPath(folder_path))
        self.active_folder = folder_path
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)
 

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
    def ui_open_folder(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.set_folder(folderpath)
    def show_welcome_tab(self):
        with open("release_notes.md", "r") as f:
            markdown = QTextEdit()
            markdown.setReadOnly(True)
            markdown.setMarkdown(f.read())
            self.tabs.addTab(markdown, QIcon("info_black_24dp.png"), "Welcome")
            f.close()
    def render(self) -> None:
        self.setup_layouts()

        self.tabs = QTabWidget()
        self.tabs.tabCloseRequested.connect(lambda index: self.tabs.removeTab(index))
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
        self.about_btn = QToolButton(self.tabs)
        self.about_btn.clicked.connect(self.show_welcome_tab)
        self.about_btn.setFixedSize(32, 32)
        self.about_btn.setIcon(QIcon("info_black_24dp.png"))

        self.file_explorer = FileExplorer()
        self.cont_layout.addWidget(self.file_explorer)
        self.cont_layout.addWidget(self.cont_editor)
        
        self.qa_layout.addWidget(self.open_folder_btn)
        self.qa_layout.addWidget(self.save_btn)
        self.qa_layout.addWidget(self.settings_btn)
        self.qa_layout.addWidget(self.about_btn)
        self.qa_layout.addStretch()

        self.cont_editor_layout.addWidget(self.qa)
        self.cont_editor_layout.addWidget(self.tabs)

        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

    def post_render(self):
        if sys.argv[1] != None:
            self.file_explorer.render_folder(sys.argv[1])

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Nadie")
        self.setMinimumSize(840, 720)
        self.resize(1080, 720)

        self.render()
        self.post_render()

def main():
    app = QApplication()
    win = Window()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
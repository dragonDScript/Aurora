from os import path
from PySide6.QtWidgets import QTabWidget, QPlainTextEdit, QTextEdit, QFileDialog
from PySide6.QtGui import QIcon
class Tabs(QTabWidget):
    file_tabs_open = {}

    def add_file_tab_signal(self, index):
        file_path = index.model().filePath(index)
        already_open = None
        for i in self.file_tabs_open:
            if self.file_tabs_open[i] == file_path:
                already_open = True
                break
        if already_open == True:
            return
        file_name = path.basename(file_path)
        editor = QPlainTextEdit()
        with open(file_path, 'r') as f:
            editor.setPlainText(f.read())
            f.close()
        index = self.addTab(editor, file_name)
        self.file_tabs_open[index] = file_path

    def ui_open_folder(self):
        while self.count():
            self.removeTab(self.currentIndex())
        self.file_tabs_open = {}
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath == None or folderpath == "":
            return
        self.file_explorer_render_folder(folderpath)

    def show_welcome_tab(self):
        with open("release_notes.md", "r") as f:
            markdown = QTextEdit()
            markdown.setReadOnly(True)
            markdown.setMarkdown(f.read())
            self.addTab(markdown, self.welcome_icon, "Welcome")
            f.close()

    def tab_focus_changed_signal(self, index):
        pass

    def close_tab_signal(self, index):
        self.file_tabs_open[index] = None
        self.removeTab(index)

    def move_tab_signal(self, fromIndex, toIndex):
        path = self.file_tabs_open[fromIndex]
        self.file_tabs_open[fromIndex] = None
        self.file_tabs_open[toIndex] = path

    def overwrite_tab_file_contents(self):
        index = self.currentIndex()
        if index == -1:
            return
        editor = self.widget(index)
        plain_text = editor.toPlainText()
        with open(self.file_tabs_open[index], 'w') as f:
            f.write(plain_text)
            f.close()

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.file_explorer_render_folder = kwargs["render_folder_func"]
        self.setTabsClosable(True)
        self.setMovable(True)
        self.welcome_icon = QIcon("info_black_24dp.png")
        self.tabCloseRequested.connect(self.close_tab_signal)
        self.tabBar().tabMoved.connect(self.move_tab_signal)
        self.currentChanged.connect(self.tab_focus_changed_signal)

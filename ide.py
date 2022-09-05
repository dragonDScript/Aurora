import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QToolButton, QTextBrowser
from browser import WebBrowser

from fexplorer import FileExplorer
from tabs import Tabs

from settings import SettingsWindow
from browser import WebBrowser

settings_window = None

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

        self.file_explorer = FileExplorer()
        self.tabs = Tabs(render_folder_func=self.file_explorer.render_folder, markdown_set_text=lambda txt:self.markdown_preview.setMarkdown(txt))

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
        self.settings_btn.clicked.connect(settings_window.show)

        self.about_btn = QToolButton(self.tabs)
        self.about_btn.clicked.connect(self.tabs.show_welcome_tab)
        self.about_btn.setFixedSize(32, 32)
        self.about_btn.setIcon(QIcon("info_black_24dp.png"))

        self.browser_toggle_btn = QToolButton(self.tabs)
        self.browser_toggle_btn.clicked.connect(self.toggle_web_browser)
        self.browser_toggle_btn.setFixedSize(32, 32)
        self.browser_toggle_btn.setIcon(QIcon("baseline_language_black_24dp.png"))

        self.markdown_toggle_btn = QToolButton(self.tabs)
        self.markdown_toggle_btn.clicked.connect(self.toggle_markdown_preview)
        self.markdown_toggle_btn.setFixedSize(32, 32)
        self.markdown_toggle_btn.setIcon(QIcon("baseline_document_scanner_black_24dp.png"))

        self.file_explorer.clicked.connect(self.tabs.add_file_tab_signal)
        self.cont_layout.addWidget(self.file_explorer)
        self.cont_layout.addWidget(self.cont_editor)
        
        self.qa_layout.addWidget(self.open_folder_btn)
        self.qa_layout.addWidget(self.save_btn)
        self.qa_layout.addWidget(self.settings_btn)
        self.qa_layout.addWidget(self.about_btn)
        self.qa_layout.addWidget(self.browser_toggle_btn)
        self.qa_layout.addWidget(self.markdown_toggle_btn)
        self.qa_layout.addStretch()

        self.cont_editor_layout.addWidget(self.qa)
        
        self.horizontal_tabs_widget = QWidget()
        self.horizontal_tabs_layout = QHBoxLayout(self.horizontal_tabs_widget)
        self.horizontal_tabs_layout.addWidget(self.tabs, stretch=1)

        # Start second panes (browser, preview, etc.)
        self.browser = WebBrowser()
        self.browser.setVisible(False)
        self.horizontal_tabs_layout.addWidget(self.browser, stretch=1)

        self.markdown_preview = QTextBrowser()
        self.markdown_preview.setVisible(False)
        self.markdown_preview.setReadOnly(True)
        self.horizontal_tabs_layout.addWidget(self.markdown_preview, stretch=1)
        # End second panes (browser, preview, etc.)

        self.cont_editor_layout.addWidget(self.horizontal_tabs_widget)

    def post_render(self):
        # render folder if there is an argument or fallback to do nothing
        try:
            if sys.argv[1] != None:
                self.file_explorer.render_folder(sys.argv[1])
        except:
            return

    def toggle_markdown_preview(self):
        if self.markdown_preview.isVisible():
            self.browser.setVisible(False)
            self.markdown_preview.setVisible(False)
        else:
            self.browser.setVisible(False)
            self.markdown_preview.setVisible(True)

    def toggle_web_browser(self):
        if self.browser.isVisible():
            self.markdown_preview.setVisible(False)
            self.browser.setVisible(False)
        else:
            self.markdown_preview.setVisible(False)
            self.browser.setVisible(True)


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
    global settings_window
    settings_window = SettingsWindow()
    win = Window()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

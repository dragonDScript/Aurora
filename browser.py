from os import path

from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage

search_engine = "https://google.com/"

class WebBrowser(QMainWindow):

    def __init__(self):
        super().__init__()

        self.toolBar = QToolBar()
        self.toolBar.setMovable(False)
        self.addToolBar(self.toolBar)
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon(path.join(__file__, "..", "icons", "baseline_arrow_back_black_18dp.png")))
        self.backButton.clicked.connect(self.back)
        self.toolBar.addWidget(self.backButton)
        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon(path.join(__file__, "..", "icons", "baseline_arrow_forward_black_18dp.png")))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)
        self.refreshButton = QPushButton()
        self.refreshButton.setIcon(QIcon(path.join(__file__, "..", "icons", "baseline_refresh_black_18dp.png")))
        self.refreshButton.clicked.connect(self.refresh)
        self.toolBar.addWidget(self.refreshButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.returnPressed.connect(self.load)
        self.toolBar.addWidget(self.addressLineEdit)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = search_engine
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.webEngineView.page().urlChanged.connect(self.urlChanged)

    def load(self):
        url = QUrl.fromUserInput(self.addressLineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    def refresh(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def urlChanged(self, url):
        self.addressLineEdit.setText(url.toString())
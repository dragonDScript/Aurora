from PySide6.QtWidgets import QTreeView, QFileSystemModel

class FileExplorer(QTreeView):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedWidth(256)
    def render_folder(self, folder_path):
        self._model = QFileSystemModel(self)
        self._model.setReadOnly(False)
        self.setModel(self._model)
        self.setRootIndex(self._model.setRootPath(folder_path))
        self.active_folder = folder_path
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)
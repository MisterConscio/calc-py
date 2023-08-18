from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from config import FS_300


class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {FS_300}px;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

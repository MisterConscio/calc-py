from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit

FS_700 = 40
FS_400 = 24
FS_300 = 18
PADDING = 10
MIN_WIDTH = 500


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {FS_700}px; padding: {PADDING}px;")
        self.setMinimumHeight(FS_700 * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MIN_WIDTH)
        # self.setTextMargins(PADDING, PADDING, PADDING, PADDING)

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit

from config import FS_700, MIN_WIDTH, PADDING


class Display(QLineEdit):
    eqResquested = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {FS_700}px; padding: {PADDING}px;")
        self.setMinimumHeight(FS_700 * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MIN_WIDTH)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()

        isEnter = key in [Qt.Key.Key_Enter, Qt.Key.Key_Return]

        if isEnter:
            self.eqResquested.emit()
            return event.ignore()

        # return super().keyPressEvent(event)

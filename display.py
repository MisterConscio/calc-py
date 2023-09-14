from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit

from config import FS_700, MIN_WIDTH, PADDING
from utils import isEmpty


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {FS_700}px; padding: {PADDING}px;")
        self.setMinimumHeight(FS_700 * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MIN_WIDTH)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()

        isEnter = key in [Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Equal]
        isDelete = key in [Qt.Key.Key_Backspace, Qt.Key.Key_Delete, Qt.Key.Key_C]
        isEsc = key in [Qt.Key.Key_Escape]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isEmpty(text):
            return event.ignore()

        # return super().keyPressEvent(event)

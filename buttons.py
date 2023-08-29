from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton

from config import FS_400
from display import Display
from utils import isEmpty, isNumOrDot, isValidNumber


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(FS_400)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display = display

        self._gridMask = [
            ["C", "►", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="],
        ]

        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, btn_text in enumerate(row):
                btn = Button(btn_text)
                if not isNumOrDot(btn_text) and not isEmpty(btn_text):
                    btn.setProperty("cssClass", "specialButton")
                self.addWidget(btn, i, j)
                btn.clicked.connect(
                    self._makeBtnDisplaySlot(self._insertTextTodisplay, btn)
                )

    def _makeBtnDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(_, *args, **kwargs)

        return realSlot

    def _insertTextTodisplay(self, checked, button):
        btnText = button.text()
        newDisplayValue = self.display.text() + btnText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(btnText)

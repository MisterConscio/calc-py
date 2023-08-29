from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton

from config import FS_400
from display import Display
from info import Info
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
    def __init__(self, display: Display, info: Info, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display = display
        self.info = info
        self._equation = ""
        self.equation = "Equação"
        self._left = None
        self._right = None
        self._op = None

        self._gridMask = [
            ["C", "►", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="],
        ]

        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(self._equation)

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, btn_text in enumerate(row):
                btn = Button(btn_text)

                if not isNumOrDot(btn_text) and not isEmpty(btn_text):
                    btn.setProperty("cssClass", "specialButton")
                    self._configSpecialBtn(btn)

                self.addWidget(btn, i, j)
                slot = self._makeSlot(self._insertTextToDisplay, btn)
                self._connectBtnClicked(btn, slot)

    def _connectBtnClicked(self, btn, slot):
        btn.clicked.connect(slot)

    def _configSpecialBtn(self, btn):
        text = btn.text()

        if text == "C":
            self._connectBtnClicked(btn, self._clear)

        if text in "+-/*":
            self._connectBtnClicked(btn, self._makeSlot(self._operatorClicked, btn))

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)

        return realSlot

    def _insertTextToDisplay(self, button):
        btnText = button.text()
        newDisplayValue = self.display.text() + btnText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(btnText)

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = "Equação"
        self.display.clear()

    def _operatorClicked(self, btn):
        btnText = btn.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            print("Nenhum número foi digitado ainda")
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = btnText
        self.equation = f"{self._left} {self._op} ??"

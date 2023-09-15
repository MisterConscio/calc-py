import math

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton

from config import FS_400
from display import Display
from info import Info
from main_window import MainWindow
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
    def __init__(
        self, display: Display, info: Info, window: MainWindow, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.display = display
        self.info = info
        self.window = window
        self._equation = ""
        self.equation = "Equação"
        self._left = None
        self._right = None
        self._op = None

        self._gridMask = [
            ["C", "<", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["N", "0", ".", "="],
        ]

        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(self._equation)

    def catchSignal(self, *args):
        print("Sinal recebido: ", type(self).__name__, args)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOperator)

        for i, row in enumerate(self._gridMask):
            for j, btn_text in enumerate(row):
                btn = Button(btn_text)

                if not isNumOrDot(btn_text) and not isEmpty(btn_text):
                    btn.setProperty("cssClass", "specialButton")
                    self._configSpecialBtn(btn)

                self.addWidget(btn, i, j)
                slot = self._makeSlot(self._insertToDisplay, btn_text)
                self._connectBtnClicked(btn, slot)

    def _connectBtnClicked(self, btn, slot):
        btn.clicked.connect(slot)

    def _configSpecialBtn(self, btn):
        text = btn.text()

        if text == "C":
            self._connectBtnClicked(btn, self._clear)

        if text == "<":
            self._connectBtnClicked(btn, self.display.backspace)

        if text == "N":
            self._connectBtnClicked(btn, self._invertNumber)

        if text in "+-/*^":
            self._connectBtnClicked(btn, self._makeSlot(self._configLeftOperator, text))

        if text == "=":
            self._connectBtnClicked(btn, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)

        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = float(displayText)

        isInt = number.is_integer()

        if isInt:
            number = int(number)

        newNumber = number * -1

        self.display.setText(str(newNumber))

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = "Equação"
        self.display.clear()

    @Slot()
    def _configLeftOperator(self, text):
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showDialog("info", "Nada foi digitado")
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f"{self._left} {self._op} ??"

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showDialog("info", "Conta incompleta")
            return

        self._right = float(displayText)
        self.equation = f"{self._left} {self._op} {self._right}"

        result = "error"

        try:
            if "^" in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showDialog("error", "Divisão por zero x_x")
        except OverflowError:
            self._showDialog("error", "O resultado foi um número muito grande")

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None

        if result == "error":
            self._left = None

    def _showDialog(self, type: str, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)

        if type == "error":
            icon = msgBox.Icon.Critical
        else:
            icon = msgBox.Icon.Information

        msgBox.setIcon(icon)
        msgBox.exec()

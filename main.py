import sys

from PySide6.QtWidgets import QApplication
from buttons import Button, ButtonsGrid

from main_window import MainWindow
from display import Display
from info import Info
from styles import setupTheme


if __name__ == "__main__":
    app = QApplication(sys.argv)
    setupTheme()

    window = MainWindow()

    info = Info("42 * 2 = 84")
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    btnGrid = ButtonsGrid(display, info, window)
    window.v_layout.addLayout(btnGrid)

    window.adjsutFixedSize()
    window.show()

    app.exec()

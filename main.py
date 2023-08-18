import sys

from PySide6.QtWidgets import QApplication
from display import Display
from info import Info

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    info = Info("42 * 2 = 84")
    window.addToVLayout(info)

    display = Display()
    window.addToVLayout(display)

    window.adjsutFixedSize()
    window.show()

    app.exec()

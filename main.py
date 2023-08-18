import sys

from PySide6.QtWidgets import QApplication
from display import Display

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    display = Display()
    window.v_layout.addWidget(display)

    window.adjsutFixedSize()
    window.show()

    app.exec()

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

    btnGrid = ButtonsGrid(display)
    window.v_layout.addLayout(btnGrid)

    # btnGrid.addWidget(Button("1"), 0, 0)
    # btnGrid.addWidget(Button("2"), 0, 1)
    # btnGrid.addWidget(Button("3"), 0, 2)
    # btnGrid.addWidget(Button("4"), 1, 0)
    # btnGrid.addWidget(Button("5"), 1, 1)
    # btnGrid.addWidget(Button("6"), 1, 2)
    # btnGrid.addWidget(Button("7"), 2, 0)
    # btnGrid.addWidget(Button("8"), 2, 1)
    # btnGrid.addWidget(Button("9"), 2, 2)
    # btnGrid.addWidget(Button("0"), 3, 1, 3, 1)

    window.adjsutFixedSize()
    window.show()

    app.exec()

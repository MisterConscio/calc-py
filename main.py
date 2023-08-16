import sys

from PySide6.QtWidgets import QApplication, QLabel

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    label = QLabel("Calculadora em Python")
    label.setStyleSheet('font-size: 48px')
    window.v_layout.addWidget(label)

    window.show()

    app.exec()

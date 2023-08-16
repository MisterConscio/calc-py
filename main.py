import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Calculadora")
    central_widget = QWidget()

    v_layout = QVBoxLayout()
    central_widget.setLayout(v_layout)

    label = QLabel("Calculadora em Python")
    v_layout.addWidget(label)

    window.setCentralWidget(central_widget)
    window.show()

    app.exec()

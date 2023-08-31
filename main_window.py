from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwags) -> None:
        super().__init__(parent, *args, **kwags)

        self.setWindowTitle("Calculadora")

        self.central_widget = QWidget()

        self.v_layout = QVBoxLayout()
        self.central_widget.setLayout(self.v_layout)

        self.setCentralWidget(self.central_widget)

    def adjsutFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.initUI()

    def initUI(self):
        # Tạo các thành phần giao diện
        self.display = QLineEdit()
        self.display.setReadOnly(True)

        buttons = [
            [('7', self.numberClicked), ('8', self.numberClicked), ('9', self.numberClicked), ('/', self.operationClicked)],
            [('4', self.numberClicked), ('5', self.numberClicked), ('6', self.numberClicked), ('*', self.operationClicked)],
            [('1', self.numberClicked), ('2', self.numberClicked), ('3', self.numberClicked), ('-', self.operationClicked)],
            [('0', self.numberClicked), ('.', self.numberClicked),('=', self.calculate) , ('+', self.operationClicked)],
            [('C', self.clear)]
        ]

        # Tạo layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Thêm display và các nút vào layout
        layout.addWidget(self.display)
        for row in buttons:
            h_layout = QHBoxLayout()
            for label, func in row:
                button = QPushButton(label)
                button.clicked.connect(func)
                button.setStyleSheet("background-color: green; font-size: 20px;")
                h_layout.addWidget(button)
            layout.addLayout(h_layout)

    def numberClicked(self):
        sender = self.sender()
        self.display.setText(self.display.text() + sender.text())

    def operationClicked(self):
        sender = self.sender()
        self.display.setText(self.display.text() + " " + sender.text() + " ")

    def calculate(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error")

    def clear(self):
        self.display.clear()


def main():
    app = QApplication(sys.argv)
    calc = CalculatorApp()
    calc.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

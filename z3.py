import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.num1_field = QLineEdit()
        self.num2_field = QLineEdit()
        self.operator_field = QLineEdit()
        self.result_label = QLabel()

        self.calculate_button = QPushButton("Вычислить")
        self.calculate_button.clicked.connect(self.calculate)

        self.power_button = QPushButton("Возведение в степень")
        self.power_button.clicked.connect(self.calculate_power)

        layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        form_layout.addWidget(self.num1_field)
        form_layout.addWidget(self.operator_field)
        form_layout.addWidget(self.num2_field)
        layout.addLayout(form_layout)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.calculate_button)
        button_layout.addWidget(self.power_button)
        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        try:
            num1 = int(self.num1_field.text())
            num2 = int(self.num2_field.text())
            operator = self.operator_field.text()

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                raise ValueError("Неправильный оператор")

            self.result_label.setText(f"{num1} {operator} {num2} = {result}")
        except Exception as e:
            self.result_label.setText(f"Ошибка: {e}")

    def calculate_power(self):
        try:
            num1 = int(self.num1_field.text())
            num2 = int(self.num2_field.text())
            result = num1 ** num2
            self.result_label.setText(f"{num1}<sup>{num2}</sup> = {result}")
        except Exception as e:
            self.result_label.setText(f"Ошибка: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())

#%%

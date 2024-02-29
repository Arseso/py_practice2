import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget

class CounterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.count = 0

        self.counter_label = QLabel(str(self.count))

        self.increment_button = QPushButton("Увеличить")
        self.increment_button.clicked.connect(self.increment)

        self.reset_button = QPushButton("Сбросить")
        self.reset_button.clicked.connect(self.reset)

        layout = QVBoxLayout()
        layout.addWidget(self.counter_label)
        layout.addWidget(self.increment_button)
        layout.addWidget(self.reset_button)

        self.setLayout(layout)

    def increment(self):
        self.count += 1
        self.counter_label.setText(str(self.count))

    def reset(self):
        self.count = 0
        self.counter_label.setText(str(self.count))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CounterWindow()
    window.show()
    sys.exit(app.exec())

#%%

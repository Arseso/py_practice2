import sys

from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout, QWidget

class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Нажать")
        self.button.setCheckable(True)
        self.button.installEventFilter(self)

        self.text_field = QLineEdit()
        self.text_field.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.text_field)

        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if obj == self.button and event.type() == QEvent.MouseButtonPress:
            self.text_field.setText("Нажата")
        elif obj == self.button and event.type() == QEvent.MouseButtonRelease:
            self.text_field.setText("Отпущена")
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonWindow()
    window.show()
    sys.exit(app.exec())

#%%

#%%

#%%

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget


class MyWindow(QMainWindow):
    def __init__(self, speech_engine):
        super().__init__()

        self.speech_engine = speech_engine
        self.setWindowTitle("PyQt6 UI Example")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        self.label = QLabel("Enter some text:")
        layout.addWidget(self.label)

        self.text_box = QTextEdit()
        layout.addWidget(self.text_box)

        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.button_clicked)
        layout.addWidget(self.button)

        main_widget.setLayout(layout)

    def button_clicked(self):
        entered_text = self.text_box.toPlainText()
        self.label.setText(f"You entered: {entered_text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow(None)
    window.show()
    sys.exit(app.exec())

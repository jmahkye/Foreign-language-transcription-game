import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget


class GameStackedWidget(QStackedWidget):
    def __init__(self, styling=None):
        super().__init__()
        self.current_page_index = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz_widget = GameStackedWidget()
    quiz_widget.show()
    sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget


class QtStackedWidget(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.current_page_index = 0

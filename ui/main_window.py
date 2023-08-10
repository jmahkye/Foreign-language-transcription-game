import sys
import logging
from ui.stacked_widget import GameStackedWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget
from game_manager import GameManager


class MainWindow(QMainWindow):
    def __init__(self, speech_engine):
        super().__init__()

        self.speech_engine = speech_engine
        self.setWindowTitle("PyQt6 UI Example")
        self.setGeometry(100, 100, 400, 300)
        menubar = self.menuBar()

        # Create 'File' menu
        file_menu = menubar.addMenu('File')

        # Create 'Edit' menu
        edit_menu = menubar.addMenu('Edit')

        main_widget = GameStackedWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        main_widget.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(None)
    window.show()
    sys.exit(app.exec())

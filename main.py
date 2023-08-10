import logging
from ui.main_window import MainWindow
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(None)
    window.show()
    sys.exit(app.exec())
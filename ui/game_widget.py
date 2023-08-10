from PyQt6.QtWidgets import QWidget
from game_enum import GameState, GameType


class GameWidget(QWidget):
    def __init__(self):
        super().__init__()

    def set_ui(self, state: GameState):
        raise NotImplementedError

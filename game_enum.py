from enum import Enum


class GameType(Enum):
    NUMBER_GUESS_LISTENING_GAME = 0
    WORD_GUESS_LISTENING_GAME = 1
    GENDER_GUESS_GAME = 2


class GameState(Enum):
    START = 0
    QUESTION = 1
    CORRECT_ANSWER = 2
    INCORRECT_ANSWER = 3
    END = 4

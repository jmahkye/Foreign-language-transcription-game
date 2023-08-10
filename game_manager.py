import logging
from game_enum import GameType, GameState
from PyQt6.QtWidgets import QWidget
from random_word_generator import RandomWordGenerator
from random_number_generator import RandomNumberGenerator

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s [%(levelname)s] - %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')


class GameManager:
    def __init__(self, db_path: str = 'assets/nouns.db', num_rounds: int = 5,
                 game_type: GameType = GameType.NUMBER_GUESS_LISTENING_GAME):
        self._score_chart = num_rounds * [0]
        self._game_type = game_type
        if self._game_type == GameType.WORD_GUESS_LISTENING_GAME:
            self.question_generator = RandomWordGenerator(db_path)
        elif self._game_type == GameType.NUMBER_GUESS_LISTENING_GAME:
            self.question_generator = RandomNumberGenerator()
        else:
            self.question_generator = None
        self._num_of_rounds = num_rounds
        self._question = ""
        self._game_state = GameState.START
        self._round_cursor = 0

    def get_score(self) -> int:
        """
        :return:
        :rtype:
        """
        return sum(self._score_chart)

    def get_game_type(self) -> GameType:
        """
        :return:
        :rtype:
        """
        return self._game_type

    def set_game_type(self, game_type: GameType):
        """
        :param game_type:
        :type game_type:
        :return:
        :rtype:
        """
        self._game_type = game_type

    def check_answer(self, answer: str) -> bool:
        """
        :param answer:
        :type answer:
        :return:
        :rtype:
        """
        result = False
        if self._round_cursor <= self._num_of_rounds - 1 and self._game_state == GameState.QUESTION:
            if answer == self._question:
                result = True
                self._score_chart[self._round_cursor] = 1
            else:
                self._score_chart[self._round_cursor] = 0

            if (self._game_state == GameState.QUESTION) and (self._round_cursor < self._num_of_rounds):
                self._round_cursor += 1
                # logging.log(logging.INFO, "Round number:{0}", self._round_cursor)
        elif self._game_state == GameState.START:
            self._score_chart = self._num_of_rounds * [0]
            self._round_cursor = 0
        else:
            print(self._score_chart)

        return result

    def set_question(self) -> None:
        """
        :return:
        :rtype:
        """
        if self._game_type == GameType.NUMBER_GUESS_LISTENING_GAME:
            pass
        elif self._game_type == GameType.GENDER_GUESS_GAME:
            pass
        elif self._game_type == GameType.WORD_GUESS_LISTENING_GAME:
            pass
        else:
            pass
        return None

    def get_question(self) -> str:
        """
        :return:
        :rtype:
        """
        return self._question

    def transfer_state(self, result: bool, game_widget) -> None:
        """
        :param result:
        :type result:
        :param game_widget:
        :type game_widget:
        :return:
        :rtype:
        """
        if self._game_state == GameState.START:
            self._game_state = GameState.QUESTION
            self._question = self.question_generator.generate_question()
        elif self._game_state == GameState.QUESTION:
            if result:
                self._game_state = GameState.CORRECT_ANSWER
            else:
                self._game_state = GameState.INCORRECT_ANSWER
        elif self._game_state == GameState.CORRECT_ANSWER or self._game_state == GameState.INCORRECT_ANSWER:
            if self._round_cursor < self._num_of_rounds:
                self._game_state = GameState.QUESTION
                self._question = self.question_generator.generate_question()
            else:
                self._game_state = GameState.END
        elif self._game_state == GameState.END:
            self._game_state = GameState.START

        game_widget.set_ui(self._game_state)

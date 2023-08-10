import random
from question_generator import QuestionGenerator


class RandomNumberGenerator(QuestionGenerator):
    def __init__(self, minimum: int = 0, maximum: int = 100) -> None:
        self._current_number = 0
        self._min = minimum
        self._max = maximum

    def set_min_max(self, minimum: int = 0, maximum: int = 100) -> None:
        """
        :param minimum:
        :type minimum:
        :param maximum:
        :type maximum:
        :return:
        :rtype:
        """
        self._min = minimum
        self._max = maximum

    def generate_random_integer(self) -> int:
        """
        :return:
        :rtype:
        """
        random_range_integer = random.randint(self._min, self._max)
        return random_range_integer

    def generate_random_float(self) -> float:
        """
        :return:
        :rtype:
        """
        random_range_float = random.uniform(self._min, self._max)
        return random_range_float

    def generate_question(self) -> str:
        """
        :return:
        :rtype:
        """
        return str(self.generate_random_integer())

import sqlite3
from question_generator import QuestionGenerator


class RandomWordGenerator(QuestionGenerator):
    def __init__(self, db: str = 'assets/nouns.db') -> None:
        self.connection = sqlite3.connect(db)
        self._random_statement = """SELECT * FROM {} ORDER BY RANDOM() LIMIT 1;""".format("nouns")

    def get_random_row(self) -> str:
        """ Query a random row in the table and return the data
        :return: cur.fetchall()[0]
        """
        try:
            cur = self.connection.cursor()
            cur.execute(self._random_statement)
            word = cur.fetchall()[0]
        except Exception as e:
            return "NO WORDS FOUND "
        return word

    def change_table(self, table_name: str) -> None:
        """ Change table used in db
        :param table_name: name of table in db
        :return: None
        """
        self._random_statement = """SELECT * FROM {} ORDER BY RANDOM() LIMIT 1;""".format(table_name)

    def generate_question(self) -> str:
        return self.get_random_row()


if __name__ == '__main__':
    reader = RandomWordGenerator()
    print(reader.get_random_row())

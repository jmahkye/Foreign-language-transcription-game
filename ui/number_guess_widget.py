import sys
import pyttsx3
import logging
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QStackedWidget
from speech_engine_pyttsx3 import TextToSpeechPyttsx3
from ui.game_widget import GameWidget
from game_manager import GameManager
from game_enum import GameType, GameState

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class NumberGuessWidget(GameWidget):
    def __init__(self, game_manager, voice_engine, styling=None):
        super().__init__()

        self.game_manager = game_manager
        self.voice_engine = voice_engine
        layout = QVBoxLayout()

        self.output_label = QLabel("")
        layout.addWidget(self.output_label)

        self.input_label = QLineEdit()
        layout.addWidget(self.input_label)

        # Set as submit to begin with
        self.proceed_button = QPushButton("Submit")
        self.proceed_button.clicked.connect(self.submit_answer)
        layout.addWidget(self.proceed_button)

        self.play_sound_button = QPushButton("Play Sound")
        self.play_sound_button.clicked.connect(self.play_question)
        layout.addWidget(self.play_sound_button)

        self.game_manager.set_game_type(GameType.NUMBER_GUESS_LISTENING_GAME)

        self.setLayout(layout)

        self.set_ui(GameState.START)

    def submit_answer(self):
        # Change the game state depending on result of the answer check
        self.game_manager.transfer_state(self.game_manager.check_answer(self.input_label.text()), self)

    def play_question(self):
        self.voice_engine.speak(self.game_manager.get_question())

    def set_ui(self, state: GameState):
        if state == GameState.START:
            self.output_label.setText("Click start")
            self.proceed_button.setText("Start")
        elif state == GameState.QUESTION:
            self.output_label.setText("What number is being said?")
            self.proceed_button.setText("Submit")
            self.input_label.setText("")
            self.play_question()
        elif state == GameState.CORRECT_ANSWER:
            self.output_label.setText("Correct")
            self.proceed_button.setText("Next")
        elif state == GameState.INCORRECT_ANSWER:
            self.output_label.setText("Incorrect")
            self.proceed_button.setText("Next")
        elif state == GameState.END:
            self.input_label.setText("")
            self.output_label.setText("Finished")
            self.proceed_button.setText("Done")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = TextToSpeechPyttsx3(pyttsx3)
    print(engine.available_voices())
    engine.set_voice(engine.available_voices()[-1])
    game_manager = GameManager("../assets/nouns.db")
    quiz_widget = NumberGuessWidget(game_manager, engine)
    quiz_widget.show()
    sys.exit(app.exec())

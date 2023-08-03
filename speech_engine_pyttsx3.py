import pyttsx3
import platform
import ispeech_engine


class TextToSpeechPyttsx3(ispeech_engine.ITextToSpeech):
    def __init__(self, engine):
        """
        :param engine:
        :type engine:
        """
        super().__init__()
        try:
            self.engine = engine.init()
            self.update_voices()
        except Exception as e:
            print(e)

    def set_voice(self, specified_voice):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if specified_voice in voice.name:
                self.engine.setProperty('voice', voice.id)
                break

    def speak(self, text):
        """
        :param text:
        :type text:
        :return:
        :rtype:
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def available_voices(self):
        """
        :return:
        :rtype:
        """
        return self.voices

    def close(self):
        """
        :return:
        :rtype:
        """
        self.engine.stop()

    def update_voices(self):
        """
        :return:
        :rtype:
        """
        voices = self.engine.getProperty('voices')
        for voice in voices:
            self.voices.append(voice.name)

    def set_voice_rate(self, voice_rate):
        """
        :param voice_rate:
        :type voice_rate:
        :return:
        :rtype:
        """
        self.engine.setProperty('rate', voice_rate)

    def get_voice_rate(self):
        """
        :return:
        :rtype:
        """
        return self.engine.getProperty('rate')

    def set_voice_volume(self, volume):
        """
        :param volume:
        :type volume:
        :return:
        :rtype:
        """
        self.engine.setProperty('volume', volume)

    def get_voice_volume(self):
        """
        :return:
        :rtype:
        """
        return self.engine.getProperty('volume')


if __name__ == "__main__":
    tts = TextToSpeechPyttsx3(pyttsx3)

    tts.set_voice('French')

    text_to_read = "12345"

    tts.speak(text_to_read)

    # tts.close()

class ITextToSpeech:
    def __init__(self):
        self.engine = None
        self.voices = []

    def set_voice(self, specified_voice):
        raise NotImplementedError

    def speak(self, text):
        raise NotImplementedError

    def available_voices(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def update_voices(self):
        raise NotImplementedError

    def set_voice_rate(self, voice_rate):
        raise NotImplementedError

    def get_voice_rate(self):
        raise NotImplementedError

    def set_voice_volume(self, volume):
        raise NotImplementedError

    def get_voice_volume(self):
        raise NotImplementedError

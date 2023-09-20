from characterai import PyCAI
import speech_recognition as sr
import gtts
from pygame import mixer as mix
import time


class Bot:
    def __init__(self, mixer: str = None, token_characterai: str = None, char_characterai: str = None, language: str = 'en') -> None:
        """
        Initializes the bot.

        Args:
            token_characterai (str): The token of characterai.
            char_characterai (str): The char is id chat characterai.
            language (str): The language of the speech to be recognized.
            mixer (str): The pygame.mixer of the bot.
        """

        self.token_characterai: str = token_characterai
        self.char_characterai: str = char_characterai
        self.language: str = language
        self.mixer: str = mixer

    def speech_to_text(self) -> str:
        """
        Converts speech to text from microphone into text.

        Returns:
            text (str): The resognized text
        """

        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio, language=self.language)
                return text
            
            except sr.UnknownValueError:
                print("Unable to recognize speech")

            except sr.RequestError as e:
                print(f"Error occurred: {e}")


    def generate_text_characterai(self, text: str) -> str:
        """
        Generates and returns a text using characterai.

        Args:
            text (str): text to send to characterai.

        Returns:
            str: The generated text.
        """

        client = PyCAI(self.token_characterai)
        client.start()
        
        chat = client.chat.get_chat(self.char_characterai)

        participants = chat['participants']

        if not participants[0]['is_human']:
            tgt = participants[0]['user']['username']
        else:
            tgt = participants[1]['user']['username']

        data = client.chat.send_message(chat['external_id'], tgt, text)
        return data['replies'][0]['text']
        

    def text_to_speech(self, text: str, file_url: str) -> None:
        """
        Converts text to speech.

        Args:
            text (str): The text to be converted to speech.
            file_url (str): The address to save the file.
        """

        tts = gtts.gTTS(text, lang=self.language)
        tts.save(file_url)
        return file_url


    def play_speech(self, file_url: str) -> None:
        """
        Plays the audio file.

        Args:
            file_url (str): The address of the file.
        """

        if self.mixer:
            mix.init(self.mixer)
        else: 
            mix.init()
        mix.music.load(file_url)
        mix.music.play()
        while mix.music.get_busy():
            time.sleep(1)


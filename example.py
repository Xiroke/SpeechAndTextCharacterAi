from SpeenchAndTextBot import Bot


bot = Bot(
    language='en', 
    token_characterai='546c30a69839f1002420c8dac010bb8cc726838d',
    char_characterai='oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254'
    )


def main():
    text = bot.speech_to_text()
    generated_text = bot.generate_text_characterai(text)
    bot.text_to_speech(generated_text, 'text.mp3')
    bot.play_speech('text.mp3')


if __name__ == '__main__':
    main()
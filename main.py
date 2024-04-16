# main.py connects gemini.py with function.py, and it also houses all the pathing and text to speech and speech to text code
import functions
import gemini
# to be changed to text to speech at a later date (using input as it is easier for testing)
while True:
    user_input = input("What can I be of help?")

    keyword = gemini.get_keyword(user_input)

    print(keyword)

    if keyword == "time":
        functions.check_time()
    elif keyword == "quit":
        functions.quit_program()
    elif keyword == "play_music":
        song = gemini.ask_gemini(f"what song does the user want to play in the following prompt, respond with only the exact song name, no singers, writers etc, leave the name in lowercase prompt:{user_input} ")
        functions.play_track(song)
    elif keyword == "pause_music":
        functions.pause_music()
    elif keyword == "skip_music":
        functions.skip_music()
    elif keyword == "search":
        sq = gemini.ask_gemini(f"what does the user want to search in the following prompt, only answer with what the user wants. prompt:{user_input}")
        functions.search(sq)
    elif keyword == "translate":
        text = gemini.ask_gemini(f"what text does the user want to be translated from the following prompt. only return the text itself. prompt:{user_input}")
        end_language = gemini.ask_gemini(f"what language does the user want his text to be translated to, return with google workspace language codes. prompt:{user_input}")
        start_language = gemini.ask_gemini(f"what is the language of the text the user wants to translate,for example if the user says'translate testing to spanish' you should return en as testing is english return the google workspace language code. prompt:{user_input}")
        print(text, end_language, start_language)
        functions.translate(text=text, start_language=start_language, end_language=end_language)
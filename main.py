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
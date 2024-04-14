# main.py connects gemini.py with function.py, and it also houses all the pathing and text to speech and speech to text code

import gemini

# to be changed to text to speech at a later date (using input as it is easier for testing)
while True:
    user_input = input("What can I be of help?")

    keyword = gemini.get_keyword(user_input)

    print(keyword)
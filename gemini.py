# gemini.py is only for the api connection to gemini in order to find our what the user wants

import textwrap
import google.generativeai as genai
from IPython.display import Markdown
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import os
from dotenv import load_dotenv


# Load variables from .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def get_keyword(input):
  response = model.generate_content(f"Expected Keyword: 'calendar' for checking the calender, 'task' for adding a task in the calendar, 'news' for checking the news, ''stock” for checking the price of a stock, “crypto” for checking the price of a cryptocurrency, 'translate' for Language Translation, and 'recipe' for Recipe Finder, ‘quit’ for quitting the program, ‘sleep’, for pausing the program,’play_music’ for playing music,’pause_music’ for pausing music, ‘skip_music’ for skipping a song/playing the next song, ‘check_email’ for checking emails,’send_email’ for sending emails, ‘search’ for searching the web,’make_file’ for making files, ‘sort_files’ for sorting files,'time' for checking the time. use these keywords. only answer with the keyword which is a correct summary the following prompt, do not use any inverted commas or spaces in front or behind the word. for example, only return 'time' not '_time_'. prompt:'{input}'")
  response = str(response.text)
  return response

def ask_gemini(input):
  response = model.generate_content(input)
  response = str(response.text)
  return response

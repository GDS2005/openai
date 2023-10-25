import pyttsx3
import openai  # for calling the OpenAI API
from decouple import config

"""
TEXT TO SPEECH
"""
#Initialize the engine
ENGINE = pyttsx3.init()
ENGINE.setProperty('rate', 160)
ENGINE.setProperty('voice', 'spanish')
ENGINE.setProperty('volume', 1)

def speak(TEXT):
    if ENGINE._inLoop:
        ENGINE.endLoop()
    ENGINE.say(TEXT)
    ENGINE.runAndWait()

"""
OPEN.AI
"""
# models
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"

openai.api_key = config('GPT_API_KEY')

def api_openai(question):

    current = "En no más de 2 parrafos;" +  question
    
    response = openai.ChatCompletion.create(
        messages=[
            {'role': 'system', 'content': 'You answer questions'},
            {'role': 'user', 'content': current},
        ],
        model=GPT_MODEL,
        temperature=0,
    )

    print("Narrador> ",response['choices'][0]['message']['content'])
    #speak(response['choices'][0]['message']['content'])
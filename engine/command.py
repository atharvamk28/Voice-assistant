import eel
import speech_recognition as sr
import pyttsx3
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from environment variable
OPENAI_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_KEY

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
r = sr.Recognizer()

messages = [{"role": "user", "content": "Please act like JARVIS from Iron Man.Your name is also JARVIS and you have a sense of humour as well."}]

def SpeakText(command):
    engine.say(command)
    engine.runAndWait()

def record_text():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("I'm Listening")
            eel.DisplayMessage('Listening.....')
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            return MyText
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        eel.DisplayMessage('Could not request result')
    except sr.UnknownValueError:
        print("Unknown Error")
        eel.DisplayMessage('Unknown Error')
    return ""

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    message = response.choices[0].message['content']
    messages.append({"role": "assistant", "content": message})
    return message

# Expose a function to start the speech recognition and AI interaction
@eel.expose
def start_interaction():
    messages = [{"role": "user", "content": "Please act like JARVIS from Iron Man."}]
    response = send_to_chatGPT(messages)
    SpeakText(response)
    print(response)
    eel.DisplayMessage(response)
    
    # Start listening for the next command
    listen_for_next_command()

def listen_for_next_command():
    while True:
        text = record_text()
        if text:
            messages.append({"role": "user", "content": text})
            response = send_to_chatGPT(messages)
            SpeakText(response)
            print(response)
            eel.DisplayMessage(response)
        else:
            print("Error in recording text, retrying...")







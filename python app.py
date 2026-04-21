import os
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return None

def ask_ai(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )

    return response.choices[0].message.content

# Main loop
speak("Voice AI started. Say something.")

while True:
    query = listen()

    if query:
        if query.lower() in ["exit", "stop", "bye"]:
            speak("Goodbye!")
            break

        answer = ask_ai(query)
        speak(answer)

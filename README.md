# LearnFusion_VoiceAssistant
Creating a basic voice assistant in Python involves several steps, including capturing audio input, recognizing speech, processing commands, and responding with synthesized speech. Below is an outline of how to implement a simple voice assistant using libraries such as `speech_recognition` for speech-to-text, `pyttsx3` for text-to-speech, and `pyaudio` for capturing audio.

### Step 1: Install Required Libraries

First, you need to install the required libraries. You can install them using pip:

bash
pip install SpeechRecognition pyttsx3 pyaudio


### Step 2: Capturing Audio and Recognizing Speech

You can use the `speech_recognition` library to capture audio and recognize speech.

python
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Could not request results from the speech recognition service.")
        return ""

# Example usage:
command = listen()


### Step 3: Text-to-Speech

Use the `pyttsx3` library to convert text to speech.

python
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage:
speak("Hello, how can I help you?")


### Step 4: Putting It All Together

Combine the above steps to create a simple voice assistant that listens for a command, processes it, and responds accordingly.

python
import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Could not request results from the speech recognition service.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def voice_assistant():
    speak("Hello, how can I help you?")
    while True:
        command = listen().lower()
        if "stop" in command:
            speak("Goodbye!")
            break
        elif "hello" in command:
            speak("Hello! How are you?")
        elif "your name" in command:
            speak("I am your voice assistant.")
        else:
            speak("I am sorry, I didn't catch that.")

# Example usage:
voice_assistant()

### Notes:
- Ensure your microphone is set up correctly and the required audio drivers are installed.
- The example uses Google Web Speech API for speech recognition, which requires an internet connection. For offline speech recognition, you might need a different library or API.

This simple implementation can be extended with more sophisticated command processing and additional functionalities as needed.

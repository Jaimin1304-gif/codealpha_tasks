import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you?")

# 🟢 Text-based input instead of voice input
def take_command():
    return input("Type your command: ").lower()

def run_assistant():
    greet()
    while True:
        command = take_command()

        if "wikipedia" in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except Exception as e:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif "open youtube" in command:
            speak("Opening YouTube")
            pywhatkit.playonyt("YouTube")

        elif "open google" in command:
            speak("Opening Google")
            pywhatkit.search("Google")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time}")

        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Searching that online for you.")
            pywhatkit.search(command)

# Run the assistant
run_assistant()

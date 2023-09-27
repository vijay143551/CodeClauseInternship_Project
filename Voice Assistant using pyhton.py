import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize the recognizer and engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print('You said:', command)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please repeat.")
        return take_command()
    except sr.RequestError:
        speak("I'm having trouble connecting to the internet. Please try again later.")
        return take_command()
    return command

# Function to perform actions based on voice commands
def run_assistant():
    speak("Hello, I'm your voice assistant. How can I assist you today?")
    while True:
        command = take_command()
        if 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak('The current time is ' + current_time)
        elif 'date' in command:
            current_date = datetime.date.today().strftime('%B %d, %Y')
            speak('Today is ' + current_date)
        elif 'search' in command:
            query = command.replace('search', '')
            try:
                result = wikipedia.summary(query, sentences=2)
                speak('Here is what I found on Wikipedia: ' + result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak('There are multiple results. Please specify your query.')
            except wikipedia.exceptions.PageError as e:
                speak('I could not find any information on that topic.')
        elif 'goodbye' in command:
            speak('Goodbye! Have a great day!')
            break
        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    run_assistant()

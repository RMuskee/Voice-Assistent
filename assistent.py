
import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble with the speech recognition service.")
        return ""

def set_reminder():
    speak("Sure, what should I remind you about?")
    reminder_text = listen()
    if reminder_text:
        speak("When should I remind you?")
        reminder_time = listen()
        # You can implement your reminder logic here using the reminder_text and reminder_time

def create_todo():
    speak("What task would you like to add to your to-do list?")
    todo_text = listen()
    if todo_text:
        # You can implement your to-do list logic here using the todo_text
        pass

def search_web():
    speak("What would you like to search the web for?")
    search_query = listen()
    if search_query:
        url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
        webbrowser.open(url)

# Main program loop
while True:
    speak("How can I assist you?")
    user_input = listen().lower()    
    if "reminder" in user_input:
        set_reminder()
    elif "to-do" in user_input:
        create_todo()
    elif "search" in user_input or "web" in user_input:
        search_web()
    elif "exit" in user_input or "quit" in user_input:
        speak("Goodbye!")
        break

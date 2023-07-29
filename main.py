import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
from websites import websites
from code_format import format_code
from ai import ai
import check_time

stop_flag = False

def speak(text, voice_id=0):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        r.pause_threshold = 1.5
        try:
            print("recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"Query: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return "Couldn't understand. Please try again."
        except sr.RequestError:
            return "Speech Recognition API is unavailable."

def stop():
    global stop_flag
    stop_flag = True
    speak("Stopping program")

def play_on_yt(query):
    pywhatkit.playonyt(query)

def open_website(website):
    print(f"Opening {website}")
    webbrowser.open(website, new=2)

def extract_website_name(query):
    words = query.split()
    website_names = [word for word in words if word.lower() in websites]
    if website_names:
        return website_names[0].lower()
    return None

def tell_time():
    time = check_time.check_time()
    speak(time)

def start():
    global stop_flag
    while not stop_flag:
        speak("Listening...")
        print("Listening...")
        command = take_command()
        if len(command) <= 1:
            speak("Couldn't understand. Please try again.")
        if "youtube" in command:
            play_on_yt(command.replace("youtube", ""))
        elif "website" in command:
            website_name = extract_website_name(command)
            if website_name and website_name in websites:
                website_url = websites[website_name]
                open_website(website_url)
        elif "the time" in command:
            tell_time()
        elif "thank you" in command:
            speak("You're welcome")
        elif "hello" in command:
            speak("Hello sir how can I help you?")
        elif "stop" in command:
            stop()
        elif "code" in command or "python" in command or "javascript" in command:
            speak("Writing code...")
            result = ai(command)
            language = "javascript" if "javascript" in command else "python"
            format_code(result, language)
            speak(f"An {language} file has been created in the current directory")
        else:
            speak("please wait...")
            result = ai(command)
            speak(result)

if __name__ == "__main__":
    start()

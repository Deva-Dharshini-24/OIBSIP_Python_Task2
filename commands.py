from datetime import datetime
import webbrowser
import os

from notes import save_note, read_notes
from weather import get_weather


def execute_command(command, speak):

    command = command.lower()

    # --------------------
    # APP LAUNCHER
    # --------------------

    apps = {
        "calculator": "calc",
        "notepad": "notepad",
        "paint": "mspaint",
        "command prompt": "cmd"
    }

    for app, command_name in apps.items():

        if app in command:

            os.system(command_name)

            speak(f"Opening {app}")

            return True

    # --------------------
    # TIME
    # --------------------

    if "time" in command:

        current_time = datetime.now().strftime("%H:%M")

        speak(f"The time is {current_time}")

    # --------------------
    # DATE
    # --------------------

    elif "date" in command:

        current_date = datetime.now().strftime("%d %B %Y")

        speak(f"Today is {current_date}")

    # --------------------
    # WEBSITES
    # --------------------

    elif "google" in command:

        webbrowser.open("https://google.com")

        speak("Opening Google")

    elif "youtube" in command:

        webbrowser.open("https://youtube.com")

        speak("Opening YouTube")

    elif "github" in command:

        webbrowser.open("https://github.com")

        speak("Opening GitHub")

    elif "linkedin" in command:

        webbrowser.open("https://linkedin.com")

        speak("Opening LinkedIn")

    # --------------------
    # SEARCH PERSON
    # --------------------

    elif "who is" in command:

        query = command.replace("who is", "").strip()

        webbrowser.open(
            f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
        )

        speak(f"Searching for {query}")

    # --------------------
    # SEARCH TOPIC
    # --------------------

    elif "search" in command:

        query = command.replace("search", "").strip()

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        speak(f"Searching for {query}")

    # --------------------
    # NOTES
    # --------------------

    elif "take note" in command:

        note = command.replace("take note", "").strip()

        save_note(note)

        speak("Note saved")

    elif "read notes" in command:

        notes = read_notes()

        speak(notes)

    # --------------------
    # WEATHER
    # --------------------

    elif "weather in" in command:

        city = command.replace(
            "weather in",
            ""
        ).strip()

        weather = get_weather(city)

        speak(weather)

        return True

    # --------------------
    # EXIT
    # --------------------

    elif "exit" in command:

        speak("Goodbye")

        return False

    # --------------------
    # UNKNOWN COMMAND
    # --------------------

    else:

        speak("Sorry, I don't know that command yet.")

    return True
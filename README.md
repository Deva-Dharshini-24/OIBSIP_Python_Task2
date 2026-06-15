# 🤖 OIBSIP — Task 2: JARVIS AI Voice Assistant

> **Intern Name:** Your Name Here
> **Task Number:** Task 2
> **Domain:** Python / Artificial Intelligence
> **Organization:** Oasis Infobyte
> **Submission Date:** June 2025

---

## 🎯 Objective

Build a fully functional AI-powered desktop Voice Assistant named **JARVIS** using Python. The assistant listens to voice commands, processes them, and responds with speech output — supporting web search, app launching, weather updates, note-taking, command history, and a modern GUI.

---

## Features Implemented

### 1. Voice Recognition
- Captures real-time microphone input using `SpeechRecognition`
- Adjusts for ambient noise automatically
- Converts speech to text using Google Speech API
- Returns recognized command as lowercase string

### 2. Text-to-Speech Output
- Uses `pyttsx3` for offline text-to-speech
- Speaks responses back to the user in real time
- Prints output to console simultaneously for debugging

### 3. Command Processing (commands.py)
Modular command handler with these capabilities:

| Voice Command | Action |
|---|---|
| "time" | Speaks current time |
| "date" | Speaks today's date |
| "open calculator" | Launches Windows Calculator |
| "open notepad" | Launches Notepad |
| "open paint" | Launches MS Paint |
| "open command prompt" | Launches CMD |
| "google" | Opens google.com |
| "youtube" | Opens youtube.com |
| "github" | Opens github.com |
| "linkedin" | Opens linkedin.com |
| "who is [name]" | Opens Wikipedia page |
| "search [topic]" | Google search |
| "take note [text]" | Saves note to file |
| "read notes" | Reads saved notes aloud |
| "weather in [city]" | Fetches live weather |
| "exit" | Shuts down assistant |

### 4. Live Weather (weather.py)
- Integrates with OpenWeatherMap API
- Fetches real-time temperature and weather description
- Displays in GUI weather panel and speaks it aloud

### 5. Notes System (notes.py, save_note.py, read_note.py)
- Saves voice-dictated notes to notes.txt
- Read notes back via voice or GUI panel
- Persistent storage across sessions

### 6. Command History (history.py)
- Logs every recognized command to history.txt
- Viewable from the GUI history panel

### 7. Wikipedia Search (__test_wiki.py)
- Fetches Wikipedia article summaries via REST API
- Uses User-Agent header for compliant API access

### 8. Modern GUI (gui.py)
- Built with CustomTkinter for a sleek dark-mode interface
- 4-panel navigation: Assistant, Weather, Notes, History
- Live status indicator (Listening / Online)
- Scrollable conversation history box
- One-click "TAP TO SPEAK" button

---

## Tools and Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core programming language |
| SpeechRecognition | Microphone input and Google STT |
| pyttsx3 | Offline text-to-speech engine |
| CustomTkinter | Modern dark-mode GUI framework |
| requests | Weather API and Wikipedia API calls |
| OpenWeatherMap API | Live weather data |
| Wikipedia REST API | Article summaries |
| webbrowser | Open URLs in default browser |
| os | Launch desktop applications |
| datetime | Time and date commands |

---

## File Structure

```
OIBSIP_WebDev_Task2/
|
|-- main.py              <- Entry point (CLI mode, no GUI)
|-- gui.py               <- GUI entry point (CustomTkinter)
|-- commands.py          <- All command logic and routing
|-- listen.py            <- Microphone input and speech recognition
|-- speak.py             <- Text-to-speech output
|-- weather.py           <- OpenWeatherMap API integration
|-- notes.py             <- Save and read notes (combined)
|-- save_note.py         <- Save note utility
|-- read_note.py         <- Read note utility
|-- history.py           <- Command history logger
|-- __test_wiki.py       <- Wikipedia API search utility
|-- notes.txt            <- Persistent notes storage (auto-created)
|-- requirements.txt     <- All Python dependencies
|-- README.md            <- This documentation file
```

---

## How to Run

### Step 1 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2A — Run with GUI (Recommended)

```bash
python gui.py
```

### Step 2B — Run in CLI / Terminal Mode

```bash
python main.py
```

### Step 3 — Use Voice Commands

Click "TAP TO SPEAK" and say any command listed in the features table above.

---

## Requirements (requirements.txt)

```
SpeechRecognition
pyttsx3
customtkinter
requests
pyaudio
```

Note on PyAudio (Windows): If pip install pyaudio fails, use:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Configuration

### Weather API Key
In weather.py, replace the API key with your own from openweathermap.org:

```python
API_KEY = "your_openweathermap_api_key_here"
```

### Default Weather City
In gui.py, change the default city:

```python
weather = get_weather("YourCity")
```

---



---

## Demo Video

YouTube Demo: [Insert YouTube Link Here]
LinkedIn Post: [Insert LinkedIn Post Link Here]

---

## Steps Performed

1. Set up project structure with modular Python files
2. Implemented speech recognition using SpeechRecognition + Google STT
3. Built text-to-speech response system using pyttsx3
4. Created command routing engine with 15+ voice command handlers
5. Integrated OpenWeatherMap API for live weather data
6. Built persistent note-taking system with file I/O
7. Added command history logging to text file
8. Integrated Wikipedia REST API for person/topic search
9. Designed modern dark-mode GUI using CustomTkinter
10. Connected all modules in both main.py (CLI) and gui.py (GUI) entry points

---

## Outcome

A fully working offline-capable AI desktop assistant that:
- Recognizes and processes natural voice commands
- Responds with synthesized speech
- Provides real-time weather, web search, and app control
- Features a professional dark-mode GUI
- Persists notes and command history across sessions

---

## File Naming Convention (As per OIBSIP Guidelines)

YourName_Task2 — e.g., RaviKumar_Task2

---

Submitted as part of the Oasis Infobyte Python / AI Internship — OIBSIP

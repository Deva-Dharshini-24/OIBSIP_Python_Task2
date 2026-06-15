from speak import speak
from listen import listen
from commands import execute_command
from history import log_command

speak("Hello, I am your voice assistant")

running = True

while running:

    command = listen()

    if command:

        log_command(command)

        running = execute_command(command, speak)
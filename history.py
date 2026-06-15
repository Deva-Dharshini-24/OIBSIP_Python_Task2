def log_command(command):

    with open("history.txt", "a") as file:

        file.write(command + "\n")

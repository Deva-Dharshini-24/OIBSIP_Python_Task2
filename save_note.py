def save_note(note):

    with open("notes.txt", "a") as file:

        file.write(note + "\n")

def read_notes():

    try:

        with open("notes.txt", "r") as file:

            return file.read()

    except:

        return "No notes found"

def read_notes():

    try:

        with open("notes.txt", "r") as file:

            return file.read()

    except:

        return "No notes found"

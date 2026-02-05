NOTES_FILE = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    print("Note saved ✔")

def view_notes():
    print("\n📒 Your Notes")
    try:
        with open(NOTES_FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No notes found.")
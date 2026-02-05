from assistant.quiz import start_quiz
from assistant.notes import add_note, view_notes
from assistant.tips import show_tips

def menu():
    print("\n📘 Digital Learning Assistant")
    print("1. Learning Tips")
    print("2. Take a Quiz")
    print("3. Add Study Note")
    print("4. View Notes")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        show_tips()
    elif choice == "2":
        start_quiz()
    elif choice == "3":
        add_note()
    elif choice == "4":
        view_notes()
    elif choice == "5":
        print("Good luck with your learning! 🚀")
        break
    else:
        print("Invalid choice. Try again.")
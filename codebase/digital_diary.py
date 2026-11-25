from datetime import datetime
FILE_NAME = "diary.txt" 
def load_notes():
    notes = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split("|", 1)
                notes.append([parts[0], parts[1]])
    return notes

def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        for note in notes:
            file.write(note[0] + "|" + note[1] + "\n")

def is_valid_date(date_text):
    if len(date_text) != 10:
        return False
    try:
        datetime.strptime(date_text, "%Y-%m-%d") 
        return True
    except ValueError:
        return False

def print_note(number, note):
    print(number, "|", note[0], "|", note[1])

def add_note():
    notes = load_notes()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not is_valid_date(date):
        print("Invalid date. Use YYYY-MM-DD.")
        return
    text = input("Enter note text: ").strip()
    if text == "":
        print("Note text cannot be empty.")
        return
    notes.append([date, text])
    save_notes(notes)
    print("Note saved.")
    print_note(len(notes), notes[-1])

def view_notes():
    notes = load_notes()
    if len(notes) == 0:
        print("No notes found. Your diary is empty.")
        return
    number = 1
    for note in notes:
        print_note(number, note)
        number = number + 1

def search_notes():
    notes = load_notes()
    keyword = input("Enter keyword to search: ").strip().lower()
    if keyword == "":
        print("Keyword cannot be empty.")
        return
    found = []
    number = 1
    for note in notes:
        if note[1].lower().find(keyword) != -1:
            found.append([number, note])
        number = number + 1
    if len(found) == 0:
        print("No notes found with that keyword.")
        return
    print("Found", len(found), "notes:")
    for item in found:
        print_note(item[0], item[1])

def delete_note():
    notes = load_notes()
    number_text = input("Enter note number to delete: ").strip()
    if not number_text.isdigit():
        print("Invalid note number.")
        return
    number = int(number_text)
    if number < 1 or number > len(notes):
        print("Note number", number, "not found.")
        return
    notes.pop(number - 1)
    save_notes(notes)
    print("Note", number, "deleted. Notes left:", len(notes))


def main():
    while True:
        print("===== DIGITAL DIARY =====")
        print("1. Add note")
        print("2. View all notes")
        print("3. Search notes")
        print("4. Delete note")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-5.")

main()

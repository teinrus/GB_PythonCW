import datetime
import json
import os


class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_date = None
        self.updated_date = None

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_date = datetime.date.today().isoformat(),


def load_notes():
    notes = []
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    return notes


def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)


def list_notes(notes):
    for note in notes:
        print(
            f"ID: {note['id']},"
            f" Заголовок: {note['title']}, "
            f"Описание: {note['body']}, "
            f"Дата создания: {note['created_date']}, "
            f"Дата изменения: {note['updated_date']}")


def add_note(notes, title, body):
    new_id = len(notes) + 1
    new_note = {"id": new_id, "title": title, "body": body, "created_date": datetime.date.today().isoformat(),
                "updated_date": None}
    notes.append(new_note)
    print("Заметка добавлена")


def edit_note(notes, note_id, title, body):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["body"] = body
            note["updated_date"] = datetime.date.today().isoformat(),
            print("Заметка изменена")
            return
    print(f"Заметки с таким ID {note_id} не найдено.")


def delete_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            print(f"Заметки с таким ID {note_id} удалена.")
            return
    print(f"Заметки с таким ID {note_id} не найдено.")


def filter_notes_by_date(notes, date):
    filtered_notes = [note for note in notes if note["created_date"] == date]
    if not filtered_notes:
        print(f"Заметок на эту дату нет: {date}")
    else:
        print(f"На {date} заметки:")
        list_notes(filtered_notes)

def main():
    notes = load_notes()
    flag = True
    while (flag):
        print("\nЗаметки:")
        print("1. Показать")
        print("2. Добавить")
        print("3. Изменить")
        print("4. Удалить")
        print("5. Поиск по дате")
        print("6. Выход")

        choice = input("Введите команду: ")
        match choice:
            case '1':
                list_notes(notes)
            case '2':
                title = input("Введите заголовок: ")
                body = input("Введите описание: ")
                add_note(notes, title, body)
            case '3':
                note_id = int(input("Введите ID для изменения: "))
                title = input("Новый заголовок: ")
                body = input("Новое описание: ")
                edit_note(notes, note_id, title, body)
            case '4':
                note_id = int(input("Введите ID для удаления: "))
                delete_note(notes, note_id)

            case '5':
                date = input("Введите дату (YYYY-MM-DD): ")
                filter_notes_by_date(notes, date)
            case '6':
                save_notes(notes)
                flag = False



if __name__ == "__main__":
    main()

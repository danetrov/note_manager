from datetime import datetime, date

notes = []


def create_note():
    note = {}

    username = input("Введите имя пользователя: ")
    while not username:
        print("Пожалуйста укажите имя")
        username = input("Введите имя пользователя: ")

    title = input("Введите заголовок: ")
    while not title:
        print("Пожалуйста введите заголовок")
        title = input("Введите заголовок: ")

    content = input("Описание заметки: ")
    while not content:
        print("Пожалуйста укажите описание заметки")
        content = input("Описание заметки: ")

    statuses = ["выполнено", "в процессе", "отложено"]
    print("Выберите статус заметки (введите цифру от 1 до 3):")
    for i, status in enumerate(statuses, start=1):
        print(f"{i}. {status}")
    while True:
        try:
            choice = int(input("Ваш выбор: "))
            if 1 <= choice <= len(statuses):
                status = statuses[choice - 1]
                break
            else:
                print("Выберите номер из списка (от 1 до 3)")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    created_date = date.today()
    print("Текущая дата:", f"{created_date.day}-{created_date.month}-{created_date.year}")

    while True:
        try:
            issue_date = input("Введите дату дедлайна (dd-mm-yyyy): ")
            issue_date = datetime.strptime(issue_date, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Пожалуйста, введите дату корректно (например 01-01-2021): ")

    note = {
        "Имя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": f"{created_date.day}-{created_date.month}-{created_date.year}",
        "Дедлайн": f"{issue_date.day}-{issue_date.month}-{issue_date.year}"
    }

    return note


def display(notes):
    if not notes:
        print("У вас нет сохранённых заметок.")
    else:
        print("\nВот что получилось:")
        print("---------------------")
        for note_id, note in enumerate(notes, start=1):
            print(f"Заметка №{note_id}:")
            for key, value in note.items():
                print(f"{key}: {value}")
            print("---------------------")


def update_note(notes):
    display(notes)

    if not notes:
        print("Нет доступных заметок для обновления.")
        return

    try:
        note_index = int(input("Введите номер заметки для обновления: ")) - 1
        if note_index < 0 or note_index >= len(notes):
            print("Некорректный номер заметки.")
            return

        note = notes[note_index]

        print("Текущая заметка:")
        for key, value in note.items():
            print(f"{key}: {value}")

        while True:
            choice = input("\nВведите название поля для изменения, например: Имя (или Enter для выхода): ")
            if choice == "":
                break
            elif choice in note:
                new_choice = input(f"Введите новое значение для {choice}: ")
                note[choice] = new_choice
                print("Заметка успешно обновлена")
            else:
                print("Такого значения нет, попробуйте еще раз.")

        print("Обновленная заметка:")
        for key, value in note.items():
            print(f"{key}: {value}")

    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")


def delete_note(notes):
    if not notes:
        print("Нет доступных заметок для удаления.")
        return
    display(notes)

    try:
        note_index = int(input("Введите номер заметки для удаления: ")) - 1
        if note_index < 0 or note_index >= len(notes):
            print("Такой заметки не существует.")
            return

        note = notes[note_index]

        print("Текущая заметка:")
        for key, value in note.items():
            print(f"{key}: {value}")

        while True:
            answ = input("Вы действительно хотите удалить эту заметку? (да/нет): ").lower()
            if answ == "да":
                del notes[note_index]
                print("Заметка успешно удалена.")
                break
            elif answ == "нет":
                print("Удаление отменено.")
                break
            else:
                print("Не понимаю вас, ответьте пожалуйста только да или нет.")

    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")


def search_note():

    if not notes:
        print("Нет доступных заметок для поиска.")
        return

    while True:
        keyword = input("Введите слово для поиска нужной заметки: ").upper()
        found_notes = [note for note in notes if (keyword in note["Имя"].upper() or
                                                  keyword in note["Заголовок"].upper() or
                                                  keyword in note["Описание"].upper() or
                                                  keyword in note["Статус"].upper())]
        if found_notes:
            for note in found_notes:
                print("Вот ваша заметка:")
                for key, value in note.items():
                    print(f"{key}: {value}")
            break
        else:
            print("Заметки с таким словом не существует, попробуйте еще раз.")


if __name__ == "__main__":
    while True:
        try:
            print("Меню действий:")
            main_choice = int(input("1. Создать новую заметку\n"
                                    "2. Показать все заметки\n"
                                    "3. Обновить заметку\n"
                                    "4. Удалить заметку\n"
                                    "5. Найти заметки\n"
                                    "6. Выйти из программы\n"
                                    "Выберите действие: "))
            if main_choice == 6:
                print("Программа завершена. Спасибо за использование!")
                break


            elif main_choice == 1:
                while True:
                    created_note = create_note()
                    notes.append(created_note)
                    while True:
                        ans = input("Хотите добавить еще одну заметку? (да/нет): ").lower()
                        if ans == 'да':
                            break
                        elif ans == 'нет':
                            exit_loop = True
                            break
                        else:
                            print("Не понимаю вас, ответьте пожалуйста только да или нет")
                    if ans == 'нет':
                        break

            elif main_choice == 2:
                display(notes)

            elif main_choice == 3:
                update_note(notes)

            elif main_choice == 4:
                delete_note(notes)

            elif main_choice == 5:
                search_note()

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
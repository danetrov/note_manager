from datetime import datetime, date

print("Добро пожаловать в Менеджер заметок!")
notes = {}
note_id = 1
dny = ["день", "дня", "дней"]

while True:
    qwe = input("Хотите добавить новую заметку? (да/нет): ")

    if qwe.lower() in ["да", "lf", "da"]:

        username = input("Введите имя пользователя: ")
        while not username:
            print("Пожалуйста укажите имя")
            username = input("Введите имя пользователя: ")

        titles = []
        while True:
            title = input("Введите заголовок (или нажмите Enter для перехода к следующему шагу): ")
            if title == "":
                break
            titles.append(title)
            unique = list(set(titles))

        content = input("Описание заметки: ")
        while not content:
            print("Пожалуйста укажите описание заметки")
            content = input("Описание заметки: ")

        statuses = ["выполнено", "в процессе", "отложено"]
        status = print("Выберите статус заметки(введите цифру от 1 до 3): ")
        for i, status in enumerate(statuses, start=1):
            print(f"{i}. {status}")
        while True:
            try:
                choice = int(input("Ваш выбор: "))
                if 1 <= choice <= len(statuses):
                    status = statuses[choice - 1]
                    break
                else:
                    print("Выберите номер из списка(от 1 до 3)")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")

        today = date.today()
        print("Текущая дата:", f"{today.day}-{today.month}-{today.year}")

        while True:
            try:
                created_date = input("Дата создания заметки (dd-mm-yyyy): ")
                created_date = datetime.strptime(created_date, "%d-%m-%Y").date()
                break
            except ValueError:
                print("Пожалуйста, введите дату корректно(например 01-01-2021): ")

        while True:
            try:
                issue_date = input("Введите дату дедлайна(dd-mm-yyyy): ")
                issue_date = datetime.strptime(issue_date, "%d-%m-%Y").date()
                break
            except ValueError:
                print("Пожалуйста, введите дату корректно(например 01-01-2021): ")

        diff = (issue_date - today)
        term = diff
        if diff.days > 0:
            if diff.days == 1:
                term = f"{'Внимание! Остался'} {diff.days} {dny[0]}"
            elif diff.days == 2 or diff.days == 3 or diff.days == 4:
                term = f"{'осталось:'} {diff.days} {dny[1]}"
            else:
                term = f"{'осталось:'} {diff.days} {dny[2]}"

        elif diff.days < 0:
            if -diff.days == 1:
                term = f"{'дедлайн истек'} {-diff.days} {dny[0]} {'назад'}"
            elif -diff.days == 2 or -diff.days == 3 or -diff.days == 4:
                term = f"{'дедлайн истек'} {-diff.days} {dny[1]} {'назад'}"
            else:
                term = f"{'дедлайн истек'} {-diff.days} {dny[2]} {'назад'}"

        else:
            term = "Внимание! Дедлайн сегодня"

        notes[note_id] = {
            "Имя": username,
            "Заголовок": ", ".join(titles),
            "Описание": content,
            "Статус": status,
            "Дата создания": f"{created_date.day}-{created_date.month}-{created_date.year}",
            "Дедлайн": f"{issue_date.day}-{issue_date.month}-{issue_date.year}, {term}"
        }

        note_id += 1

    elif qwe.lower() in ["нет", "ytn", "net"]:
        break
    else:
        print("Не понимаю вас, ответьте пожалуйста только да или нет")

print("Вот что получилось:\n")
for note_id, note in notes.items():
    print(f"Заметка {note_id}:")
    for key, value in note.items():
        print(f"{key}: {value}")
    print()

actions = ["Удалить заметку", "Обновить статус", "Показать заметки", "Выйти"]

print("Список действий:")
action = print("Выберете действие которое хотите сделать(введите цифру под нужным действием): ")

for i, action in enumerate(actions, start=1):
    print(f"{i}. {action}")

while True:
    try:
        choice = int(input("\nВаш выбор: "))

        if choice == 4:
            break

        elif choice == 1:
            while True:
                deleteS = input("Введите номер заметки, которую хотите удалить (или нажмите Enter для выхода): ")
                if deleteS == "":
                    break
                try:
                    delete = int(deleteS)
                    if delete in notes:
                        del notes[delete]
                        print(f"\nЗаметка {delete} была удалена")
                    else:
                        print("Такой заметки не существует. Попробуйте снова.")
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите число.")

        elif choice == 2:
            while True:
                new_status_idS = input(
                    "Введите номер заметки, в которой хотите обновить статус(или Enter для выхода): ")
                if new_status_idS == "":
                    break
                try:
                    new_status_id = int(new_status_idS)

                    if new_status_id in notes:
                        current_status = notes[new_status_id]["Статус"]
                        print(f"Текущий статус: {current_status}")
                        print("Выберите новый статус заметки: ")
                        for i, status in enumerate(statuses, start=1):
                            print(f"{i}. {status}")
                        while True:
                            try:
                                choices = int(input("\nВаш выбор: "))
                                if 1 <= choices <= len(statuses):
                                    new_status = statuses[choices - 1]
                                    notes[new_status_id]["Статус"] = new_status
                                    print("Статус заметки успешно обновлён на: " + new_status)
                                    break
                                else:
                                    print("Выберите номер из списка(от 1 до 3)")
                            except ValueError:
                                print("Некорректный ввод. Пожалуйста, введите число.")
                    else:
                        print("Такой заметки не существует. Попробуйте снова.")
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите число.")

        elif choice == 3:
            print("Вот что получилось:\n")
            for note_id, note in notes.items():
                print(f"Заметка {note_id}:")
                for key, value in note.items():
                    print(f"{key}: {value}")
                print()

        else:
            print("Выберите цифру из предложенных от 1 до 4")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")

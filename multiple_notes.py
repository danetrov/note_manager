# Работа с несколькими заметками

print("Добро пожаловать в 'Менеджер заметок'!")

notes = []
while True: # Основной бесконечный цикл
    qwe = input("Хотите добавить новую заметку? (да/нет): ")

    if qwe == "да" or qwe == "lf" or qwe == "LF" or qwe == "ДА" or qwe == "Да" or qwe == "Lf":
        username = input("Имя пользователя: ")
        while True:
            if username == "":
                print("Пожалуйста укажите имя")
                username = input("Имя пользователя: ")
            else:
                break
        title = input("Заголовок заметки: ")
        while True:
            if title == "":
                print("Пожалуйста укажите заголовок")
                title = input("Заголовок заметки: ")
            else:
                break
        content = input("Описание заметки: ")
        while True:
            if content == "":
                print("Пожалуйста укажите описание заметки")
                content = input("Описание заметки: ")
            else:
                break
        status = input("Статус заметки: ")
        while True:
            if status == "":
                print("Пожалуйста укажите статус заметки")
                status = input("Статус заметки: ")
            else:
                break
        created_date = input("Дата создания заметки (dd-mm-yyyy): ")
        while True:
            if created_date == "":
                print("Пожалуйста укажите дату создания заметки (dd-mm-yyyy)")
                created_date = input("Дата создания заметки (dd-mm-yyyy): ")
            else:
                break
        issue_date = input("Дата истечения заметки (dd-mm-yyyy): ")
        while True:
            if issue_date == "":
                print("Пожалуйста дату истечения заметки")
                issue_date = input("Дата истечения заметки (dd-mm-yyyy): ")
            else:
                break

        notes.append(username)
        notes.append(title)
        notes.append(content)
        notes.append(status)
        notes.append(created_date)
        notes.append(issue_date)

    elif qwe == "нет" or qwe == "ytn" or qwe == "YTN" or qwe == "НЕТ" or qwe == "Нет" or qwe == "Ytn":
        break
    else:
        print("Не понимаю вас, ответьте пожалуйста да/нет")

print("Вот что получилось:\n")

for index, item in enumerate(notes):
    number = (index % 6) + 1

    if number == 1 and index != 0:
        print()

    print(f"{number}. {item}")






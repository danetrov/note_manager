print("Добро пожаловать в 'Менеджер заметок'!")
notes = {}
note_id = 1

def display(notes):
    if not notes:
        print("У вас нет сохранённых заметок")
    else:
        print("\nВот что получилось:")
        print("---------------------")
        for note_id, note in notes.items():
            print(f"Заметка №{note_id}:")
            for key, value in note.items():
                print(f"{key}: {value}")
            print("---------------------")

while True:
    qwe = input("Хотите добавить новую заметку? (да/нет): ")

    if qwe.lower() in ["да", "lf"]:
        username = input("Имя пользователя: ")
        while not username:
            print("Пожалуйста укажите имя")
            username = input("Имя пользователя: ")

        title = input("Заголовок заметки: ")
        while not title:
            print("Пожалуйста укажите заголовок")
            title = input("Заголовок заметки: ")

        content = input("Описание заметки: ")
        while not content:
            print("Пожалуйста укажите описание заметки")
            content = input("Описание заметки: ")

        status = input("Статус заметки: ")
        while not status:
            print("Пожалуйста укажите статус заметки")
            status = input("Статус заметки: ")

        created_date = input("Дата создания заметки (dd-mm-yyyy): ")
        while not created_date:
            print("Пожалуйста укажите дату создания заметки (dd-mm-yyyy)")
            created_date = input("Дата создания заметки (dd-mm-yyyy): ")

        issue_date = input("Дата истечения заметки (dd-mm-yyyy): ")
        while not issue_date:
            print("Пожалуйста укажите дату истечения заметки")
            issue_date = input("Дата истечения заметки (dd-mm-yyyy): ")

        notes[note_id] = {
            "Имя": username,
            "Заголовок": title,
            "Описание": content,
            "Статус": status,
            "Дата создания": created_date,
            "Дедлайн": issue_date
        }

        note_id += 1

    elif qwe.lower() in ["нет", "ytn"]:
        break
    else:
        print("Не понимаю вас, ответьте пожалуйста да/нет")

display(notes)
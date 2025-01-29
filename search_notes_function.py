notes = [
    {'Имя': 'Алексей',
     'Заголовок': 'Список покупок',
     'Описание': 'Купить продукты на неделю',
     'Статус': 'новая',
     'Дата создания': '27-11-2024',
     'Дедлайн': '30-11-2024'},

    {'Имя': 'Мария',
     'Заголовок': 'Учеба',
     'Описание': 'Подготовиться к экзамену',
     'Статус': 'в процессе',
     'Дата создания': '25-11-2024',
     'Дедлайн': '01-12-2024'},

    {'Имя': 'Иван',
     'Заголовок': 'План работы',
     'Описание': 'Завершить проект',
     'Статус': 'выполнено',
     'Дата создания': '20-11-2024',
     'Дедлайн': '26-11-2024'}
]
# Поиск по имени
def search_note():
    while True:
        name = input("Введите имя для поиска нужной заметки: ").upper()
        found_notes = [note for note in notes if note["Имя"].upper() == name]
        if found_notes:
            for note in found_notes:
                print("Вот ваша заметка:")
                for key, value in note.items():
                    print(f"{key}: {value}")
            break
        else:
            print("Заметки с таким пользователем не существует, попробуйте еще раз.")
search_note()
# Поиск по статусу
def search_note():
    while True:
        status = input("Введите статус для поиска нужной заметки: ").upper()
        found_notes = [note for note in notes if note["Статус"].upper() == status]
        if found_notes:
            for note in found_notes:
                print("Вот ваша заметка:")
                for key, value in note.items():
                    print(f"{key}: {value}")
            break
        else:
            print("Заметки с таким пользователем не существует, попробуйте еще раз.")
search_note()
# Поиск по слову
def search_note():
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
search_note()
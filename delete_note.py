notes = [
    {"username": "Алексей",
     "title": "Список покупок",
     "content": " Купить продукты на неделю"},
    {"username": "Мария",
     "title": "Учеба",
     "content": "Подготовиться к экзамену"}
]
print("Текущие заметки:")
for index, note in enumerate(notes, start=1):
        print(f"{index}. Имя: {note['username']}\n   "
              f"Заголовок: {note['title']}\n   "
              f"Описание: {note['content']}\n")

while True:

    answer = input("Хотите удалить заметку?(да/нет): ")

    if answer.lower() == "да":
        operation = input("Введите имя пользователя для удаления заметки: ")
        found = False

        while not found:
            operation = input("Введите имя пользователя для удаления заметки: ")

            for note in notes:

                if note["username"].lower() == operation.lower():
                    notes.remove(note)
                    print("Заметка", {note["title"]}, "удалена")
                    found = True
                    break

            if not found:
                print("Такого пользователя не существует, повторите ввод корректно")


    elif answer == "нет":
        print("Текущие заметки:")
        for index, note in enumerate(notes, start=1):
            print(f"{index}. Имя: {note['username']}\n   "
              f"Заголовок: {note['title']}\n   "
              f"Описание: {note['content']}\n")
        break
    else:
        print("Некорректный ввод, напишите да/нет")




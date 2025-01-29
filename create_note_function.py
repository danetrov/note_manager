from datetime import datetime, date

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

created_date = date.today()
print("Текущая дата:", f"{created_date.day}-{created_date.month}-{created_date.year}")

while True:
    try:
        issue_date = input("Введите дату дедлайна(dd-mm-yyyy): ")
        issue_date = datetime.strptime(issue_date, "%d-%m-%Y").date()
        break
    except ValueError:
        print("Пожалуйста, введите дату корректно(например 01-01-2021): ")

note = {
    "Имя": username,
    "Заголовок": title,
    "Описание": content,
    "Статус": status,
    "Дата создания": f"{created_date.day}-{created_date.month}-{created_date.year}",
    "Дедлайн": f"{issue_date.day}-{issue_date.month}-{issue_date.year}"
}

print("Вот что получилось:\n")
for key, value in note.items():
    print(f"{key}: {value}")
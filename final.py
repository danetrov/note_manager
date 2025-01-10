username = input("Имя пользователя: ")
title = input("Заголовок заметки: ")
content = input("Описание заметки: ")
status = input("Статус заметки: ")
temp_created_date = input("Дата создания заметки (dd-mm-yyyy): ")
created_date = (temp_created_date[:5])
temp_issue_date = input("Дата истечения заметки (dd-mm-yyyy): ")
issue_date = (temp_issue_date[:5])
main = input("Основная тема: ")
headline = input("Заголовок: ")
subtitle = input("Подзаголовок: ")

spisok = [username, title,
          main,
          headline, subtitle, content,
          status,
          created_date,
          issue_date]
print("Вот что получилось: ")
for index, item in enumerate(spisok):
    print(f"{index + 1}. {item}")

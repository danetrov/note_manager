username = input("Имя пользователя: ")
title = input("Заголовок заметки: ")
content = input("Описание заметки: ")
status = input("Статус заметки: ")
created_date = input("Дата создания заметки (dd-mm-yyyy): ")
issue_date = input("Дата истечения заметки (dd-mm-yyyy): ")

main = input("Основная тема: ")
headline = input("Заголовок: ")
subtitle = input("Подзаголовок: ")

spisok = [username, title, [main, headline, subtitle], content, status, created_date, issue_date]
print(spisok)

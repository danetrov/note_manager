from datetime import datetime, date

a = date.today()
print("Текущая дата:", a.day,"-", a.month,"-", a.year) # Выводим текущую дату

dny = ["день", "дня", "дней"] #Список со склонением слово день для корректного вывода

while True: #цикл для неправильного ответа пользователя
    try: #блок для исключения ошибки в дате

        issue_date = input("\nВведите дату дедлайна(yyyy-mm-dd): ")
        issue_date = datetime.strptime(issue_date, "%Y-%m-%d") #Преобразуем формат
        issue_date = issue_date.date() #команда для корректной работы сравнения дат,преобразуем datetime -> date

        diff = (issue_date - a) #Разница дат

        if diff.days > 0:
            if diff.days == 1:
                print("До дедлайна осталось: ", diff.days, dny[0])
            elif diff.days == 2 or diff.days == 3 or diff.days == 4:
                print("До дедлайна осталось: ", diff.days, dny[1])
            else:
                print("До дедлайна осталось: ", diff.days, dny[2])

        elif diff.days < 0:
            if -diff.days == 1:
                print("Внимание! Дедлайн истек: ", -diff.days, dny[0], "назад")
            elif -diff.days == 2 or -diff.days == 3 or -diff.days == 4:
                print("Внимание! Дедлайн истек: ", -diff.days, dny[1], "назад")
            else:
                print("Внимание! Дедлайн истек: ", -diff.days, dny[2], "назад")

        else:
            print("Дедлайн сегодня")

        break

    except ValueError:
        print("Пожалуйста, введите дату корректно: ")

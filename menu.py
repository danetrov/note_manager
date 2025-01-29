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
            continue

        elif main_choice == 2:
            continue

        elif main_choice == 3:
            continue

        elif main_choice == 4:
            continue

        elif main_choice == 5:
            continue

    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")

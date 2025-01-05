statuses = ["выполненно", "в процессе", "отложено"]

current_status = "в процессе"
print("Текущий статус заметки: " + current_status)

print("\nВыберите новый статус заметки:")
for i, status in enumerate(statuses, start=1):
        print(f"{i}. {status}")
while True:
    try:
        choice = int(input("\nВаш выбор: "))
        if  1 <= choice <= len(statuses):
            current_status = statuses[choice -1]
            print("Статус заметки успешно обновлён на: " + current_status)
            break
        else:
            print("Выберите номер из списка(от 1 до 3)")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")
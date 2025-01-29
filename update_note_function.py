update_note = {
    'username': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '27-11-2024',
    'issue_date': '30-11-2024'
}
print("Текущая заметка:")
for key, value in update_note.items():
    print(f"{key}: {value}")

while True:

    choice = input("\nВведите значение которое хотите поменять(или Enter для выхода): ")

    if choice == "":
        break

    elif choice in update_note:
        new_choice = input(f"Введите новое значение для {choice}: ")
        update_note[choice] = new_choice

    else:
        print("Такого значения нет, Введите еще раз значение которое хотите поменять(например: username)")

print("Текущая заметка:")
for key, value in update_note.items():
    print(f"{key}: {value}")

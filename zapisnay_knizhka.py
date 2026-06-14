while True:
    print("\n1 - Добавить заметку")
    print("2 - Показать все заметки")
    print("3 - Выйти")

    vibor = input("Выберите: ")

    if vibor == "1":
        zametka = input("Введите заметку: ")
        try:
            with open("C:\\Users\\komam\\notes.txt", "a", encoding="utf-8") as f:
                f.write(zametka + "\n")
            print("Сохранено!")
        except:
            print("Ошибка! не удалось сохранить заметку")

    elif vibor == "2":
        try:
            with open("C:\\Users\\komam\\notes.txt", "r", encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("Заметок пока нет!")

    elif vibor == "3":
        print("GOOD BYE!")
        break

    else:
        print("Неверный выбор! Введи 1, 2, или 3.")
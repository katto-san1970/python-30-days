while True:
    try:
        number_1 = float(input("Введите 1-ое число: "))
        number_2 = float(input("Введите 2-ое число: "))
        operaciya = input("Введите операцию( +  -  /  *) или 'exit' для выхода: ")

        if operaciya == "exit":
            print("Пока!")
            break

        elif operaciya == "+":
            print("Ответ: ", number_1 + number_2)
        
        elif operaciya == "-":
            print("Ответ: ", number_1 - number_2)
            
        elif operaciya == "/":
            if number_2 == 0:
                print("Ошибка, на 0 делить нельзя.")
            else:
                rezultat = number_1 / number_2
                if rezultat == int(rezultat):
                    print("Ответ:", int(rezultat))
                else:
                    print("Ответ:", float(f"{rezultat:.10g}"))
            
        elif operaciya == "*":
            print("Ответ: ", number_1 * number_2)

        else:
            print("Неверная операция! Введи +, -, / или *")
    
    except ValueError:
        print("Ошибка! Введи число, а не текст.")
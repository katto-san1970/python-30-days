number = 42
popitki = 0

while True:
    a = int(input("Угадайте число: "))
    popitki = popitki + 1

    if a > number:
        print("Меньше")
    elif a < number:
        print("Больше")
    else:            
        if popitki == 1:
            print("Угадал за 1 попытку!")
        elif popitki < 5:
            print(f"Угадал за {popitki} попытки!")
        else:
            print(f"Угадал за {popitki} попыток!")
        break
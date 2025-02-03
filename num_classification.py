number = int(input("Введите число: "))

if number % 2 == 0:
    if number % 4 == 0:
        print("Число делится на 4")
    else:
        print("Обычное четное число")
else:
    if number % 5 == 0:
        print("Число делится на 5")
    else:
        print("Просто нечетное число")
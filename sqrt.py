import math
import datetime

sqrt_25 = math.sqrt(25)
pi_value = math.pi
cos_45 = math.cos(math.radians(45))
current_datetime = datetime.datetime.now()

print(f"Квадратный корень из 25: {sqrt_25}")
print(f"Значение π: {pi_value}")
print(f"Косинус 45 градусов: {cos_45}")

with open("results.txt", "w", encoding = "utf-8") as file:
    file.write(f"Квадратный корень из 25: {sqrt_25}\n")
    file.write(f"Значение л: {pi_value}\n")
    file.write(f"Косинус 45 градусов: {cos_45}\n")

print("Результаты в results.txt")

try:
    with open("results.txt", "r", encoding = "utf-8") as file:
        print("\nСодержимое файла results.txt: ")
        print(file.read())
        
except FileNotFoundError:
    print("Ошибка: файл results.txt не найден")

with open("results.txt", "a", encoding = "utf-8") as file:
        file.write(f"Дата и время: {current_datetime}\n")

        print("Дата и время в results.txt: ")
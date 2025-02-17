numbers = [22, 45, 67, 12, 89, 34, 55, 90, 10]
min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
        
print("Наибольшее ччисло: ", max_num)
print("Наименьшее число: ", min_num)
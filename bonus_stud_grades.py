def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
scores = list(map(int, input("Введите список оценок через пробел: ").split()))  
  
even_count = 0
odd_count = 0

print("Результаты оценок:")
for score in  scores:
    grade = get_grade(score)
    status = "Сдал" if grade != "F" else "Не сдал"
    print(f"Балл: {score} -> Оценка: {grade} ({status})")
    
    if score %2 == 0:
        even_count += 1
    else:
        odd_count +=1 
        
print(f"\nЧетных оценок: {even_count}")
print(f"Нечетных оценок: {odd_count}")
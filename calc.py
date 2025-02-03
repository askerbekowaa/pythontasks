import math

def calc(a, b, oper):
    if oper == "+":
        result = a + b
        
    elif oper == "-":
        result = a - b
        
    elif oper == "*":
        result = a * b
    
    elif oper == "/":
        if b == 0:
            print("Ошибка: деление на ноль!")
            return None
        result = a / b
        
    elif oper == "sqrt":
        result = math.sqrt(a)
    
    elif oper == "%":
        result = (a * b)/100
        
    elif oper == "^2":
        result = a ** 2
        
    elif oper == "^3":
        result = a ** 3
     
    else:
        print("Неизвестная операция!")
        return None
        
        
    print(f"{a} {oper} {b if oper != 'sqrt' else ''} = {result}")
    return result

print("Выберите операцию: ")
print("1. Сложение (+)")
print("2. Вычитание (-)")
print("3. Умножение (*)")
print("4. Деление (/)")
print("5. Извлечение квадратного корня (sqrt)")
print("6. Вычисление процента (%)")
print("7. Возведение в квадрат (^2)")
print("8. Возведение в куб (^3)")

oper_choises = {"1": "+", "2": "-", "3": "*", "4": "/", 
                "5": "sqrt", "6": "%", "7": "^2", "8": "^3"}
oper = oper_choises.get(input("Введите номер операции: "))

if oper is None:
    print("Неверный выбор операции!")
else:
    a = float(input("Введите первое число: "))
    
    if oper in ["sqrt", "^2", "^3"]:
        b = None
    else: 
        b = float(input("Введите второе число: "))
        
    if oper == "%" and b is None:
            print("Для вычисления процента необходимо ввести второе число!")
    else:
      calc(a, b, oper)
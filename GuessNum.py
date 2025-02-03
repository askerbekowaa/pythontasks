import random

def game():
    number_to_guess = random.randit(1, 100)
    tries = 0
    
    while True:
        guess = int(input("Угадай число от 1 до 100: "))
        tries += 1
        
        if guess == number_to_guess:
            print(f"Поздравляю! Ты угадал число {number_to_guess} за {tries} попыток.")
            break
        elif abs(guess - number_to_guess) <=10:
            print("Близко!")
        else:
            print("Мимо. Попробуй еще раз!")
            
if __name__== "__main":
    game()
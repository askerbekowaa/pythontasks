salary = float(input("Введите вашу зарплату в $: "))
credit_score = int(input("Введите ваш кредитный рейтинг: "))

if salary > 50000:
    if credit_score > 700:
        print("Кредит одобрен с низкой процентной ставкой.")
    else:
        print("Кредит одобрен, но с высокой процентной ставкой.")
else:
    if credit_score > 700:
        print("Кредит одобрен, но с жесткими условиями.")
    else:
        print("Кредит отклонен из-за низкой зарплаты и рейтинга.")
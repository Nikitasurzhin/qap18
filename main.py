ticketCount = int(input("Ввести количество билетов:"))
price = 0
for value in range(ticketCount):
    age = int(input("Ввести возраст"))
    if age < 18:
        price = price + 0
        print("Сумма покупки:", price, "руб")
    elif 18 <= age < 25:
        price = price + 990
        print("Сумма покупки:", price, "руб")
    elif age >= 25:
        price = price + 1390
        print("Сумма покупки:", price, "руб")
    if ticketCount > 3:
        price = price - (price/10)
        print("Цена билетов с учетом скидки", int(price), "руб")


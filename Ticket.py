try:
    tickets = int(input("Какое количество билетов Вы хотите приобрести: \t"))
    age = [int(input("Введите Ваш возраст участника и нажмите 'Enter' \t")) for i in range(tickets)]
    if tickets<0:
        raise ValueError("Ошибка ввода данных")
except ValueError as error:

    print("Неправильные данные")

price1 = 990
price2 = 1390
price3 = 0
prices = []
sales = 0.1
total_price = ''



for i in age:
    if i < 18:
        prices.append(price3)

    elif i in range(18, 25):
        prices.append(price1)
    elif i >= 25:
        prices.append(price2)
total_price = sum(prices)
if len(prices) >= 3:
    total_price = sum(prices) - sum(prices) * 0.1
print('Вы заказали:', tickets, 'билетов')
print('Возраст участников:', list(age))
print('Цены на билеты:', prices)
print('Итого:', total_price)



money = int(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

Bank1 = int((per_cent['ТКБ']) * (money/100))
Bank2 = int((per_cent['СКБ']) * (money/100))
Bank3 = int((per_cent['ВТБ']) * (money/100))
Bank4 = int((per_cent['СБЕР']) * (money/100))
Deposit = [Bank1, Bank2, Bank3, Bank4]
print('Все банковские ставки:',(Deposit))
print('Самая выгодная ставка:',(max(Deposit)))
print(per_cent.values())
print(per_cent.keys())

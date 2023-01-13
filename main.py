money = int(input('Введите планируемую сумму: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
list_values = list(per_cent.values())
deposit.append(int(list_values[0] * money / 100))
deposit.append(int(list_values[1] * money / 100))
deposit.append(int(list_values[2] * money / 100))
deposit.append(int(list_values[3] * money / 100))
print(deposit)
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))

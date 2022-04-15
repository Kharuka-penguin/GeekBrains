# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple, OrderedDict

params = ['name', 'qu_1', 'qu_2', 'qu_3', 'qu_4']
New_Company = namedtuple('New_Company', params)

quantity = int(input('\nСколько предприятий собираетесь вводить: '))
companies = [New_Company(input('\nВведите название компании: '), int(input('Введите прибыль за 1 квартал: ')),
                         int(input('Введите прибыль за 2 квартал: ')), int(input('Введите прибыль за 3 квартал: ')),
                         int(input('Введите прибыль за 4 квартал: '))) for i in range(quantity)]

summa_items = 0
average_sum_companies_dict = OrderedDict()

for item in companies:
    summa_item = item.qu_1 + item.qu_2 + item.qu_3 + item.qu_4
    average_sum_companies_dict[item.name] = summa_item
    summa_items += summa_item

average_sum_companies = summa_items / quantity
print(f'\nСредняя годовая прибыль по всем предприятиям равна {average_sum_companies}\n')

for key in average_sum_companies_dict:
    if average_sum_companies_dict[key] > average_sum_companies:
        print(f'Годовая прибыль "{key}" выше среднего')
    elif average_sum_companies_dict[key] < average_sum_companies:
        print(f'Годовая прибыль "{key}" ниже среднего')
    elif average_sum_companies_dict[key] == average_sum_companies:
        print(f'Годовая прибыль "{key}" равна среднему')

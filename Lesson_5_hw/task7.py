"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
      название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
import json


def profit(ln):
    ln = ln.split()
    return int(ln[2]) - int(ln[3])


firms = []
firms_profit = []
with open("input_file_task7.txt") as open_file:
    for line in open_file:
        firms.append(line[:line.find(' ')])
        firms_profit.append(profit(line))

for firm, prof in zip(firms, firms_profit):
    print(firm, prof)

pos_prof = [prof for prof in firms_profit if prof > 0]
average_profit = round(sum(pos_prof)/len(pos_prof), 2)
print(f"Средняя прибыль: {average_profit}")

firms_dict = {firm: prof for firm, prof in zip(firms, firms_profit)}
json_result = json.dumps([firms_dict, {"Average_profit": average_profit}])
print(json_result)

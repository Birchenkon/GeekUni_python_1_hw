"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""
from sys import argv
_, *argv = argv


def zp(val):
    val = [float(v) for v in val]
    return val[0]*val[1] + val[2]


print(zp(argv))

# _, hours, pro_hour, premium = argv
# def zp(h, p_h, prem):
#     return float(h) * float(p_h) + float(prem)
#
#
# print(zp(hours, pro_hour, premium))
"""5. Реализовать два небольших скрипта:

а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

from itertools import count, cycle
from sys import argv
from random import randint

_, count_to = argv

for el in count(int(count_to)):
    if el < int(count_to) + 10:
        print(el, end=' ')
    else:
        break

print()
c = 0
for el in cycle("ABCDE"):
    if c < int(count_to) + 10:
        print(el, end=' ')
        c += 1
    else:
        break

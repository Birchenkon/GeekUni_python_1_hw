"""6. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""
from sys import argv
_, n = argv


def fact(x):
    i = 1
    f = 1
    while i <= x:
        yield f
        i += 1
        f *= i


for el in fact(int(n)):
    print(el)

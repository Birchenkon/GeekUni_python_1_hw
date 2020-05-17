"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

sp_1 = [11, 2.1, 'ds', [10, 20], (3, 4), {"a": 1, "b": 2}]
for s in sp_1:
    print(s, type(s))

"""2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input()."""

n = int(input('Введите кол-во элементов: '))
sp_2 = [input() for i in range(n)]
print(' Было:')
for s in sp_2:
    print(s, end=' ')

for i in range(0, n-1, 2):
    sp_2[i], sp_2[i+1] = sp_2[i+1], sp_2[i]

print('\n Стало:')
for s in sp_2:
    print(s, end=' ')

"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict."""

# через list
month = ['Зима', 'Весна', 'Лето', 'Осень']
num = int(input('Введите номер месяца: '))
# когда узанла про тернарные операторы :)
print(month[num//3] if num != 12 else month[0]) if 1 <= num <= 12 else print('такого месяца нет')

# через dict
dict_month = {12: "зима", 1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна",
              6: "лето", 7: "лето", 8: "лето", 9: "осень", 10: "осень", 11: "осень"}
print(dict_month.get(num))

"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове."""

str_new = input().split(' ')
print(str_list)
for ind, s in enumerate(str_list):
    print(ind, s[:10])


"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент 
с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

my_list = [7, 5, 3, 3, 2]
new = int(input('Введите число: '))
pos = 0
while my_list[pos] >= new:
    pos += 1
my_list.insert(pos, new)
print(my_list)

"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя."""

all_products = []
ans = input('Добавить товар? да/нет \n').lower()
list_param = ['Название', 'Цена', 'Количество', 'Единицы']  # список характеристик
while ans != 'нет':
    if ans == 'да':
        product = (int(input('Номер товара: ')),
                   {list_param[0]: input(list_param[0] + ': '), list_param[1]: float(input(list_param[1] + ': ')),
                    list_param[2]: int(input(list_param[2] + ': ')), list_param[3]: input(list_param[3] + ': ')})
        all_products.append(product)
    else:
        print('Некорректный ввод')
    ans = input('Добавить товар? да/нет \n')

"""Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, 
например название, а значение — список значений-характеристик, например список названий товаров."""

all_products_dict = dict.fromkeys(list_param, [])
for key in list_param:
    all_products_dict[key] = list(set(prod[1].get(key) for prod in all_products))

for key, val in all_products_dict.items():
    print(key, ':', val)
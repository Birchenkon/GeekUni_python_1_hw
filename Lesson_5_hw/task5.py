"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
from random import randint

file_to_inp = open("input_file_task5.txt", "w")

sequence = [randint(-100, 100) for _ in range(randint(4, 15))]
for x in sequence:
    file_to_inp.write(str(x)+' ')
file_to_inp.close()

with open("input_file_task5.txt") as open_file:
    new_str = [int(x) for x in open_file.read().split()]

print(f"Сумма чисел = {sum(new_str)}")

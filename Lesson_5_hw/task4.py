"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

words_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_output = open("output_file_task4.txt", "w")

with open("input_file_task4.txt") as open_file:
    for line in open_file:
        new_line = line.split(' — ')
        new_line[0] = words_dict[new_line[0]]
        new_line = ' — '.join(new_line)
        file_output.write(new_line)

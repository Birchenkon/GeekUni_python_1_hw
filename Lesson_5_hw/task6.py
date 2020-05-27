"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""


def sum_numbers(new_line):
    st_with_num = ''
    for ch in range(len(new_line)):
        if new_line[ch].isdigit():
            st_with_num += new_line[ch]
            if not new_line[ch + 1].isdigit():
                st_with_num += ' '
    return sum([int(x) for x in st_with_num.split()])


dict_ans = {}
with open("input_file_task6.txt") as open_file:
    for line in open_file:
        dict_ans[line[:line.find(':')]] = sum_numbers(line)

print(dict_ans)

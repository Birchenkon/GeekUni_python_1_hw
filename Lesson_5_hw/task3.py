"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

cnt, summ = 0, 0
print('Сотрудники с окладом < 20 тыс.:')

with open("input_file_task3.txt") as open_file:
    for line in open_file:
        new_line = line.split()
        cnt += 1
        summ += float(new_line[1])
        if float(new_line[1]) < 20000:
            print(new_line[0])

print(f"Средняя величина дохода = {summ/cnt:.2f}")
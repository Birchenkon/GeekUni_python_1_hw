"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""


cnt_lines, cnt_words = 0, []
with open('input_file_task2.txt') as open_file:
    for line in open_file:
        cnt_lines += 1
        cnt_words.append(line.count(' ') + 1)

print(f"Количество строк = {cnt_lines}")
for num, cnt in enumerate(cnt_words):
    print(f"Строка: {num+1:2} Слов: {cnt:2}")

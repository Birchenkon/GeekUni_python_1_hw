"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

out_file = open("out_file.txt", "w")
user_inp = input() + '\n'
while user_inp != '\n':
    out_file.write(user_inp)
    user_inp = input() + '\n'
out_file.close()

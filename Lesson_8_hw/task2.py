"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой."""


class ZeroDivision(Exception):
    def __init__(self, err):
        self.err = err


if __name__ == '__main__':

    num1, num2 = float(input('Число 1 = ')), float(input('Число 2 = '))
    try:
        # result = num1 / num2
        if num2 == 0:
            raise ZeroDivision("Деление на 0")
    except ZeroDivision as e:
        print(e)
    else:
        print(f"Ответ = {num1 / num2}")



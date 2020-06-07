"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class Complex:
    def __init__(self, a1, b1, a2, b2):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2

    def __str__(self):
        return f" Первое число = ({self.a1}+{self.b1}j) \n Второе число = ({self.a2}+{self.b2}j)"

    def add(self):
        return f" Сумма = ({self.a1 + self.a2}+{self.b1 + self.b2}j)"

    def multiplication(self):
        return f" Произведение = ({self.a1 * self.a2 - self.b1 * self.b2}+" \
               f"{self.a1 * self.b2 + self.b1 * self.a2}j)"


if __name__ == "__main__":
    cmp = Complex(1, 2, 3, 4)
    print(cmp)
    print(cmp.add())
    print(cmp.multiplication())

"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn_left(self):
        return f'Машина {self.name} повернула налево'

    def turn_right(self):
        return f'Машина {self.name} повернула направо'

    def show_speed(self):
        return f'Скорость машины {self.name} : {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости {self.name} на {self.speed - 60} км/ч'
        else:
            return f'Скорость машины {self.name} : {self.speed} км/ч -- превышение на {self.speed - 40} км/ч'


class SportCar(Car):
    def show_speed(self):
        return f'Скорость машины {self.name} : {self.speed} км/ч'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость машины {self.name} : {self.speed} км/ч -- превышение на {self.speed - 40} км/ч'
        else:
            return f'Скорость машины {self.name} : {self.speed} км/ч -- в пределах нормы'


class PoliceCar(Car):
    def show_speed(self):
        return f'Скорость машины {self.name} : {self.speed} км/ч'


car = Car(120, "white", "bmw", 0)
tc = TownCar(50, "grey", "mazda", 0)
sc = SportCar(180, "red", "mclaren", 0)
wc = WorkCar(55, "black", "honda", 0)
pc = PoliceCar(150, "blue", "ford", 1)

print(f"name: {car.name:10} color: {car.color:10} speed (km/h) : {str(car.speed):10} "
      f"is police: {'no' if car.is_police == 0 else 'yes'}")
print(f"name: {tc.name:10} color: {tc.color:10} speed (km/h) : {str(tc.speed):10} "
      f"is police: {'no' if tc.is_police == 0 else 'yes'}")
print(f"name: {sc.name:10} color: {sc.color:10} speed (km/h) : {str(sc.speed):10} "
      f"is police: {'no' if sc.is_police == 0 else 'yes'}")
print(f"name: {wc.name:10} color: {wc.color:10} speed (km/h) : {str(wc.speed):10} "
      f"is police: {'no' if wc.is_police == 0 else 'yes'}")
print(f"name: {pc.name:10} color: {pc.color:10} speed (km/h) : {str(pc.speed):10} "
      f"is police: {'no' if pc.is_police == 0 else 'yes'}")

print('\n', car.go(), '\n', car.stop(), '\n', car.turn_left(), '\n', car.turn_right(), '\n', car.show_speed())
print('\n', tc.go(), '\n', tc.stop(), '\n', tc.turn_left(), '\n', tc.turn_right(), '\n', tc.show_speed())
print('\n', sc.go(), '\n', sc.stop(), '\n', sc.turn_left(), '\n', sc.turn_right(), '\n', sc.show_speed())
print('\n', wc.go(), '\n', wc.stop(), '\n', wc.turn_left(), '\n', wc.turn_right(), '\n', wc.show_speed())
print('\n', pc.go(), '\n', pc.stop(), '\n', pc.turn_left(), '\n', pc.turn_right(), '\n', pc.show_speed())

"""
Вам необходимо создать свою иерархию классов для машин.
Классы должны называться CarBase (базовый класс для всех типов машин),
Car (легковые автомобили), Truck (грузовые автомобили) и SpecMachine (спецтехника).

Все объекты имеют обязательные атрибуты:
- car_type, значение типа объекта и может принимать одно из значений: «car», «truck», «spec_machine».
- photo_file_name, имя файла с изображением машины, допустимы названия файлов изображений с расширением
  из списка: «.jpg», «.jpeg», «.png», «.gif»
- brand, марка производителя машины
- carrying, грузоподъемность

В базовом классе CarBase нужно реализовать метод get_photo_file_ext для получения расширения
файла изображения. Расширение файла можно получить при помощи os.path.splitext.

Для грузового автомобиля необходимо в конструкторе класса определить атрибуты:
body_length, body_width, body_height, отвечающие соответственно за
габариты кузова — длину, ширину и высоту. Габариты передаются в параметре
body_whl (строка, в которой размеры разделены латинской буквой «x»).
Обратите внимание на то, что характеристики кузова должны быть
вещественными числами и характеристики кузова могут быть не валидными
(например, пустая строка). В таком случае всем атрибутам, отвечающим за
габариты кузова, присваивается значение равное нулю.
Также для класса грузового автомобиля необходимо реализовать метод
get_body_volume, возвращающий объем кузова.

В классе Car должен быть определен атрибут passenger_seats_count
(количество пассажирских мест), а в классе SpecMachine — extra (дополнительное описание машины).

Обратите внимание, что у каждого объекта из иерархии должен быть свой набор атрибутов и методов.
Например, у класса легковой автомобиль не должно быть метода get_body_volume в отличие от
класса грузового автомобиля. Имена атрибутов и методов должны совпадать с теми, что описаны выше.

Далее вам необходимо реализовать функцию get_car_list, на вход которой подается имя файла
в формате csv. Файл содержит данные, аналогичные строкам из таблицы. Вам необходимо прочитать
этот файл построчно при помощи модуля стандартной библиотеки csv. Затем проанализировать строки
на валидность и создать список объектов с автомобилями и специальной техникой. Функция должна
возвращать список объектов.

Первая строка в исходном файле — это заголовок csv, который содержит имена колонок.
Нужно пропустить первую строку из исходного файла. Обратите внимание на то, что в некоторых
строках исходного файла , данные могут быть заполнены некорректно, например, отсутствовать
обязательные поля или иметь не валидное значение. В таком случае нужно проигнорировать подобные
строки и не создавать объекты. Строки с пустым или не валидным значением для body_whl игнорироваться
не должны.  Вы можете использовать стандартный механизм обработки исключений в процессе чтения,
валидации и создания объектов из строк csv-файла.

Тесты
1.
car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
Ответ:
car
Bugatti Veyron
bugatti.png
0.312
2

2.
truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height,\
                                                                                                 sep='\n')
Ответ:
truck
Nissan
nissan.jpeg
3.92
2.09
1.87

3.
spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name,\
                                                                         spec_machine.extra, sep='\n')
Ответ:
spec_machine
Komatsu-D355
93.0
d355.jpg
pipelayer specs

4.
spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
print(spec_machine.get_photo_file_ext())

Ответ:
.jpg

"""

import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        _, ext = os.path.splitext(self.photo_file_name)
        return ext


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        dimensions = body_whl.split('x')
        self.body_length = float(dimensions[0])
        self.body_width = float(dimensions[1])
        self.body_height = float(dimensions[2])
        self.car_type = 'truck'

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(file_name: str) -> list:
    try:
        car_list = []
        with open(file_name) as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                if len(row) != 7:
                    continue
                car_type = row[0]
                brand = row[1]
                photo_file_name = row[3]
                carriyng = row[5]
                if not (car_type and brand and photo_file_name and carriyng):
                    continue
                base_car = CarBase(brand, photo_file_name, carriyng)
                ext = base_car.get_photo_file_ext()
                if not (ext in ['.jpg', '.jpeg', '.png', '.gif']):
                    continue
                try:
                    carriyng = float(carriyng)
                except ValueError:
                    continue

                if car_type == 'car':
                    passenger_seats_count = row[2]
                    try:
                        passenger_seats_count = int(passenger_seats_count)
                    except ValueError:
                        continue
                    car_list.append(Car(brand, photo_file_name, carriyng, passenger_seats_count))
                elif car_type == 'truck':
                    body_whl = row[4]
                    if not body_whl:
                        body_whl = '0x0x0'
                    car_list.append(Truck(brand, photo_file_name, carriyng, body_whl))
                elif car_type == 'spec_machine':
                    extra = row[6]
                    if not extra:
                        continue
                    car_list.append(SpecMachine(brand, photo_file_name, carriyng, extra))
                else:
                    continue
        return car_list
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    list_car = get_car_list('source/cars.csv')
    for car in list_car:
        print(type(car))

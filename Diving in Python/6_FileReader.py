"""
Задача: написать python-модуль, внутрь которого необходимо поместить код класса FileReader.
Конструктор этого класса принимает один параметр: путь до файла на диске. В классе FileReader
должен быть реализован метод read, возвращающий строку - содержимое файла, путь к которому
был указан при создании экземпляра класса. Python модуль должен быть написан таким образом,
чтобы импорт класса FileReader из него не вызвал ошибок.
При написании реализации метода read, вам нужно учитывать случай, когда при инициализации
был передан путь к несуществующему файлу. Требуется обработать возникающее при этом
исключение FileNotFoundError и вернуть из метода read пустую строку.

Тесты
> python 6_FileReader.py existed_file.txt
some text

> python 6_FileReader.py not_existed_file.txt
(пусто)

"""

import sys


class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def __repr__(self):
        return 'reader'

    def read(self):
        try:
            with open(self.file_name, 'r') as f:
                text = f.read()
            return text
        except FileNotFoundError:
            return ""


if __name__ == '__main__':
    reader = FileReader(sys.argv[1])
    print(reader.read())

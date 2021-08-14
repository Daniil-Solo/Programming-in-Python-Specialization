"""
Нужно создать интерфейс для работы с файлами. Интерфейс должен предоставлять
следующие возможности по работе с файлами:
- чтение из файла, метод read возвращает строку с текущим содержанием файла
- запись в файл, метод write принимает в качестве аргумента строку с новым содержанием файла
- сложение объектов типа File, результатом сложения является объект класса File, при этом
  создается новый файл и файловый объект, в котором содержимое второго файла добавляется к
  содержимому первого файла. Новый файл должен создаваться в директории, полученной с
  помощью функции tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.
- возвращать в качестве строкового представления объекта класса File полный путь до файла
- поддерживать протокол итерации, причем итерация проходит по строкам файла
При создании экземпляра класса File в конструктор передается полный путь до файла на файловой
системе. Если файла с таким путем не существует, он должен быть создан при инициализации.

Тесты

path_to_file = 'some_filename.txt'
print(os.path.exists(path_to_file))
# False
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
# True
print(file_obj)
# some_filename.txt

file_obj_1 = File('some_filename_1.txt')
file_obj_2 = File('some_filename_2.txt')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))
# True
print(new_file_obj)
for line in new_file_obj:
    print(ascii(line))
# line 1
# line 2

new_path_to_file = str(new_file_obj)
print(os.path.exists(new_path_to_file))
# True
file_obj_3 = File(new_path_to_file)
print(file_obj_3)
# Temp\...
"""


import random
import tempfile
import os


class File:
    def __init__(self, file_name):
        self.file_path = file_name
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'x'):
                pass
        self.n_string = 0
        self.current_string_index = 0

    def read(self):
        with open(self.file_path, 'r') as f:
            string_list = f.readlines()
        self.n_string = len(string_list)
        return ''.join(string_list)

    def write(self, text):
        with open(self.file_path, 'w') as f:
            f.write(text)

    def __add__(self, other):
        text_1 = self.read()
        text_2 = other.read()
        text = text_1 + text_2

        folder_temp_path = tempfile.gettempdir() + '\\'
        new_file_name = str(hex(random.randint(a=0, b=1000000))) + '.txt'
        new_file_name = folder_temp_path + new_file_name
        new_file = File(new_file_name)
        new_file.write(text)
        return new_file

    def __str__(self):
        return self.file_path

    def __iter__(self):
        return self

    def __next__(self):
        string_list = self.read().split('\n')
        if self.current_string_index < self.n_string:
            current_string = string_list[self.current_string_index]
            self.current_string_index += 1
            return current_string
        else:
            raise StopIteration


path_to_file = 'some_filename.txt'
print(os.path.exists(path_to_file))
# False
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
# True
print(file_obj)
# some_filename.txt
file_obj_1 = File('some_filename_1.txt')
file_obj_2 = File('some_filename_2.txt')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))
# True
print(new_file_obj)
for line in new_file_obj:
    print(ascii(line))
# line 1
# line 2
new_path_to_file = str(new_file_obj)
print(os.path.exists(new_path_to_file))
# True
file_obj_3 = File(new_path_to_file)
print(file_obj_3)
# Temp\...

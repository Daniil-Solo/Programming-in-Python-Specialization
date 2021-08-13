"""
Напишите декоратор to_json, который можно применить к различным функциям,
чтобы преобразовывать их возвращаемое значение в JSON-формат. Не забудьте
про сохранение корректного имени декорируемой функции.

Тест:
Запустить скрипт
В папке с кодом должны появиться файлы get_data_1.json и get_data_2.json,
содрежащие {'data': 42} и {'data': 4, 'info': 123} соответственно
"""

import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        file_name = func.__name__ + '.json'
        with open(file_name, 'w') as f:
            json.dump(result, f)
        return result

    return wrapped


@to_json
def get_data_1():
    return {
        'data': 42
    }


@to_json
def get_data_2():
    return {
        'data': 4,
        'info': 123
    }


get_data_1()
get_data_2()

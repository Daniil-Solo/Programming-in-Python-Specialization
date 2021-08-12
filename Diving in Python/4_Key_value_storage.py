"""
Данные будут сохраняться в файле storage.data. Добавление новых данных
в хранилище и получение текущих значений осуществляется с помощью
утилиты командной строки 4_Key_value_storage.py.

Сохранение значения value по ключу key_name:
> storage.py --key key_name --val value

Получение значения по ключу key_name:
> storage.py --key key_name

Утилита может вызваться со следующими параметрами:
--key <имя ключа> , где <имя ключа> - ключ по которому сохраняются/получаются значения
--val <значение>, где <значение> - сохраняемое значение.

Если при запуске утилиты переданы оба ключа, происходит добавление переданного значения
по ключу и сохранение данных в файле. Если передано только имя ключа, происходит чтение
файла хранилища и вывод на печать значений, которые были сохранены по данному ключу.
Обратите внимание, что значения по одному ключу не перезаписываются, а добавляются к уже
сохраненным. Другими словами - по одному ключу могут храниться несколько значений.
При выводе на печать, значения выводятся в порядке их добавления в хранилище.
Формат вывода на печать для нескольких значений: value_1, value_2

Обратите внимание на пробел после запятой. Если значений по ключу не было найдено,
выведите пустую строку или None.

Тесты:
> python 4_Key_value_storage.py --key key_name --val value
> python 4_Key_value_storage.py --key key_name
value

> python 4_Key_value_storage.py --key multi_key --val value1
> python 4_Key_value_storage.py --key multi_key --val value2
> python 4_Key_value_storage.py --key multi_key
value1, value2
"""

import argparse
import tempfile
import os
import json


def storage_request(key: str, value) -> None:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    storage = dict()
    if not os.path.exists(storage_path):
        with open(storage_path, 'w') as f:
            json.dump(storage, f)
    else:
        with open(storage_path, 'r') as f:
            storage = json.load(f)

    if key in storage:
        if type(value) is str:
            storage[key].append(value)
        else:
            print(', '.join(storage[key]))
    else:
        if type(value) is str:
            storage[key] = [value]
        else:
            print()

    with open(storage_path, 'w') as f:
        json.dump(storage, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str)
    parser.add_argument('--value', default=None, type=str)
    args = parser.parse_args()
    storage_request(args.key, args.value)

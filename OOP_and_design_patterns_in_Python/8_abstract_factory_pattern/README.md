# Реализация паттерна Абстрактная фабрика
Даны шесть классов: EasyMap, EasyObjects, MediumMap, MediumObjects, HardMap, HardObjects. Каждый из классов генерирует карту и список объектов для неё.

На их основе необходимо создать абстрактную фабрику AbstractLevel c классовыми методами get_map() и get_objects(). Её реализации должны носить имена EasyLevel, MediumLevel и HardLevel.
![img.png](img.png)

## Особенности реализации
В файле main.py содержится код для тестирования
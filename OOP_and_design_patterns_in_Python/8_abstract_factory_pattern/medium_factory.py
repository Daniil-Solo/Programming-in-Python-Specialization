import random
from abstract_factory import AbstractLevel


class EasyLevel(AbstractLevel):
    class Map:
        def __init__(self):
            self._map = [[0 for j in range(8)] for i in range(8)]
            for i in range(8):
                for j in range(8):
                    if i == 0 or j == 0 or i == 7 or j == 7:
                        # граница карты
                        self._map[j][i] = -1
                    else:
                        # случайная характеристика области
                        self._map[j][i] = random.randint(0, 2)

        def get_map(self):
            return self._map

    class Objects:
        def __init__(self):
            # размещаем переход на след. уровень
            self.objects = [('next_lvl', (4, 4))]

        def get_objects(self, map_obj):
            # размещаем врагов
            for obj_name in ['rat', 'snake']:
                coord = (random.randint(1, 6), random.randint(1, 6))
                # ищем случайную свободную локацию
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 6), random.randint(1, 6))

                self.objects.append((obj_name, coord))

            return self.objects

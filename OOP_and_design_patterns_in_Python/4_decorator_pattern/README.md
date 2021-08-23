# Создание декоратора класса
Необходимо написать реализацию системы эффектов, которые могут быть наложены на героя игры. В игре есть герой, который обладает некоторым набором характеристик.

К основным характеристикам относятся: Сила (Strength), Восприятие (Perception), Выносливость (Endurance), Харизма (Charisma), Интеллект (Intelligence), Ловкость (Agility), Удача (Luck).

Враги и союзники могут накладывать на героя положительные и отрицательные эффекты. Эти эффекты изменяют характеристики героя,  увеличивая или уменьшая значения определенных характеристик, в зависимости от того какие эффекты были наложены.  На героя можно накладывать бесконечно много эффектов, действие одинаковых эффектов суммируется. Игрок должен знать, какие положительные и какие отрицательные эффекты на него были наложены и в каком порядке. Названия эффектов совпадают с названиями классов.

За получение данных о текущем состоянии героя отвечают методы `get_stats`, `get_positive_effects`,  `get_negative_effects`.

## Описание эффектов:
+ Берсерк (Berserk)
  +  Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7; 
  +  Уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
количество единиц здоровья увеличивается на 50
+ Благословение (Blessing) 
    + увеличивает все основные характеристики на 2. 
+ Слабость (Weakness)
    + уменьшает характеристики: Сила, Выносливость, Ловкость на 4.
+ Сглаз (EvilEye) 
  + уменьшает  характеристику Удача на 10.
+ Проклятье (Curse)
  + уменьшает все основные характеристики на 2.

## При выполнении задания необходимо учитывать:
* изначальные характеристики базового объекта не должны меняться.
* изменения характеристик и накладываемых эффектов (баффов/дебаффов) должны происходить динамически, то есть вычисляться при вызове методов get_stats, get_positive_effects, get_negative_effects
абстрактные классы AbstractPositive,  AbstractNegative и соответственно их потомки могут принимать любой параметр base при инициализации объекта (_ _ init _ _ (self, base))
* эффекты должны корректно сниматься, в том числе и из середины стека

## Пример
```Python
>>> # создаем героя
>>> hero = Hero()
>>> hero.get_stats()
{'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}
>>> hero.stats
{'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}
>>> hero.get_negative_effects()
[ ]
>>> hero.get_positive_effects()
[ ]
>>> # накладываем эффект

>>> brs1 = Berserk(hero)
>>> brs1.get_stats()
{'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 22, 'Perception': 1, 'Endurance': 15, 'Charisma': -1, 'Intelligence': 0, 'Agility': 15, 'Luck': 8}
>>> brs1.get_negative_effects()
[ ]
>>> brs1.get_positive_effects()
['Berserk']

>>> # накладываем эффекты
>>> brs2 = Berserk(brs1)

>>> cur1 = Curse(brs2)

>>> cur1.get_stats()
{'HP': 228, 'MP': 42, 'SP': 100, 'Strength': 27, 'Perception': -4, 'Endurance': 20, 'Charisma': -6, 'Intelligence': -5, 'Agility': 20, 'Luck': 13}
>>> cur1.get_positive_effects()
['Berserk', 'Berserk']
>>> cur1.get_negative_effects()
['Curse']
>>> # снимаем эффект Berserk
>>> cur1.base = brs1
>>> cur1.get_stats()
{'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 20, 'Perception': -1, 'Endurance': 13, 'Charisma': -3, 'Intelligence': -2, 'Agility': 13, 'Luck': 6}
>>> cur1.get_positive_effects()
['Berserk']
>>> cur1.get_negative_effects()
['Curse']
```
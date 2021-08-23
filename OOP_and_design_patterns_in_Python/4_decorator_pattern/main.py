from hero import Hero
from positive_classes import Berserk, Blessing
from negative_classes import Weakness, EvilEye, Curse


if __name__ == '__main__':
    # создаем героя
    hero = Hero()
    print(hero.get_stats())
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())
    print()

    # накладываем эффекты
    brs1 = Berserk(hero)
    bls1 = Blessing(brs1)
    cur1 = Curse(bls1)
    hero = cur1
    print(hero.get_stats())
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())
    print()

    # снимаем эффект Berserk
    cur1.base = brs1
    hero = cur1
    print(hero.get_stats())
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())
    print()

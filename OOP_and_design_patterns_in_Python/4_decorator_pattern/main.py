from hero import Hero
from positive_classes import Berserk, Blessing
from negative_classes import Weakness, EvilEye, Curse


if __name__ == '__main__':
    hero = Hero()
    print(hero.get_stats())
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())

    brs1 = Berserk(hero)
    brs2 = Blessing(brs1)
    cur1 = Curse(brs2)
    hero = cur1
    print(hero.get_stats())
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())

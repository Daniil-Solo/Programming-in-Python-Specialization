from hero import Hero
from positive_classes import Berserk, Blessing
from negative_classes import Weakness, EvilEye, Curse


if __name__ == '__main__':
    hero = Hero()
    print(hero.get_stats())
    print(hero.get_positive_effects())

    hero = Curse(hero)
    hero = Curse(hero)
    hero = Curse(hero)
    hero = Curse(hero)
    hero = Curse(hero)
    print(hero.get_stats())
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())

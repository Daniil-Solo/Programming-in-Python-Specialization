from hero import Hero
from positive_classes import Berserk, Blessing, Weakness


if __name__ == '__main__':
    hero = Hero()
    print(hero.get_stats())
    print(hero.get_positive_effects())

    hero = Weakness(Blessing(Berserk(hero)))
    print(hero.get_stats())
    print(hero.get_positive_effects())

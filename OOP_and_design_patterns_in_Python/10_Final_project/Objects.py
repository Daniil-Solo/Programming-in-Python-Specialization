from abc import ABC, abstractmethod
import pygame
import random


def create_sprite(img, sprite_size):
    icon = pygame.image.load(img).convert_alpha()
    icon = pygame.transform.scale(icon, (sprite_size, sprite_size))
    sprite = pygame.Surface((sprite_size, sprite_size), pygame.HWSURFACE)
    sprite.blit(icon, (0, 0))
    return sprite


class Interactive(ABC):

    @abstractmethod
    def interact(self, engine, hero):
        pass


class AbstractObject(ABC):
    @abstractmethod
    def draw(self, display):
        pass


class Ally(AbstractObject, Interactive):

    def __init__(self, icon, action, position):
        self.sprite = icon
        self.action = action
        self.position = position

    def interact(self, engine, hero):
        self.action(engine, hero)



class Creature(AbstractObject):

    def __init__(self, icon, stats, position):
        self.sprite = icon
        self.stats = stats
        self.position = position
        self.calc_max_HP()
        self.hp = self.max_hp

    def calc_max_HP(self):
        self.max_hp = 5 + self.stats["endurance"] * 2


class Hero(Creature):

    def __init__(self, stats, icon):
        pos = [1, 1]
        self.level = 1
        self.exp = 0
        self.gold = 0
        super().__init__(icon, stats, pos)

    def level_up(self):
        while self.exp >= 100 * (2 ** (self.level - 1)):
            yield "level up!"
            self.level += 1
            self.stats["strength"] += 2
            self.stats["endurance"] += 2
            self.calc_max_HP()
            self.hp = self.max_hp


class Effect(Hero):

    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()
        self.apply_effect()

    @property
    def position(self):
        return self.base.position

    @position.setter
    def position(self, value):
        self.base.position = value

    @property
    def level(self):
        return self.base.level

    @level.setter
    def level(self, value):
        self.base.level = value

    @property
    def gold(self):
        return self.base.gold

    @gold.setter
    def gold(self, value):
        self.base.gold = value

    @property
    def hp(self):
        return self.base.hp

    @hp.setter
    def hp(self, value):
        self.base.hp = value

    @property
    def max_hp(self):
        return self.base.max_hp

    @max_hp.setter
    def max_hp(self, value):
        self.base.max_hp = value

    @property
    def exp(self):
        return self.base.exp

    @exp.setter
    def exp(self, value):
        self.base.exp = value

    @property
    def sprite(self):
        return self.base.sprite

    @abstractmethod
    def apply_effect(self):
        pass


class Berserk(Effect):
    def __init__(self, base):
        super().__init__(base)

    def apply_effect(self):
        changing_stats = {
            "HP": 50,  # health points
            "Strength": 7,  # сила
            "Perception": -3,  # восприятие
            "Endurance": 7,  # выносливость
            "Charisma": -3,  # харизма
            "Intelligence": -3,  # интеллект
            "Agility": 7,  # ловкость
            "Luck": 7  # удача
        }
        for key in changing_stats:
            self.stats[key] += changing_stats[key]


class Blessing(Effect):
    def __init__(self, base):
        super().__init__(base)

    def apply_effect(self):
        changing_stats = {
            "HP": 2,  # health points
            "MP": 2,  # magic points,
            "SP": 2,  # skill points
            "Strength": 2,  # сила
            "Perception": 2,  # восприятие
            "Endurance": 2,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 2,  # интеллект
            "Agility": 2,  # ловкость
            "Luck": 2  # удача
        }
        for key in changing_stats:
            self.stats[key] += changing_stats[key]


class Blessing(Effect):
    def __init__(self, base):
        super().__init__(base)

    def apply_effect(self):
        changing_stats = {
            "Strength": 4,  # сила
            "Endurance": 4,  # выносливость
            "Agility": 4,  # ловкость
        }
        for key in changing_stats:
            self.stats[key] += changing_stats[key]


class Enemy(Creature, Interactive):
    def __init__(self, icon, stats, xp, position):
        self.icon = icon
        self.stats = stats
        self.xp = xp
        self.position = position

    def interact(self, engine, hero):
        pass

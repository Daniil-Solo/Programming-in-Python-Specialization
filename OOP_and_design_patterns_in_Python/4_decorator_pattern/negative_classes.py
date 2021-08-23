class AbstractNegative:
    def __init__(self, base, name, changing_stats):
        self.base = base
        self.name = name
        self.changing_stats = changing_stats

    def get_negative_effects(self):
        previous_effects = self.base.get_negative_effects()
        previous_effects.append(self.name)
        return previous_effects

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_stats(self):
        current_stats = self.base.get_stats()
        for stat_key in self.changing_stats.keys():
            current_stats[stat_key] += self.changing_stats[stat_key]
        return current_stats


class Weakness(AbstractNegative):
    name = "Weakness"
    changing_stats = {
        "Strength": 4,  # сила
        "Endurance": 4,  # выносливость
        "Agility": 4,  # ловкость
    }

    def __init__(self, base):
        super().__init__(base, Weakness.name, Weakness.changing_stats)


class EvilEye(AbstractNegative):
    name = "EvilEye"
    changing_stats = {
        "Luck": 10  # удача
    }

    def __init__(self, base):
        super().__init__(base, EvilEye.name, EvilEye.changing_stats)


class Curse(AbstractNegative):
    name = "Curse"
    changing_stats = {
        "HP": -2,  # health points
        "MP": -2,  # magic points,
        "SP": -2,  # skill points
        "Strength": -2,  # сила
        "Perception": -2,  # восприятие
        "Endurance": -2,  # выносливость
        "Charisma": -2,  # харизма
        "Intelligence": -2,  # интеллект
        "Agility": -2,  # ловкость
        "Luck": -2  # удача
    }

    def __init__(self, base):
        super().__init__(base, Curse.name, Curse.changing_stats)

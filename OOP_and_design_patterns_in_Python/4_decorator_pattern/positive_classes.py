from absctract_effect import AbstractEffect


class AbstractPositive(AbstractEffect):
    def __init__(self, base, name, changing_stats):
        super().__init__(base, name, changing_stats)

    def get_positive_effects(self):
        previous_effects = super().get_positive_effects()
        previous_effects.append(self.name)
        return previous_effects


class Berserk(AbstractPositive):
    name = "Berserk"
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

    def __init__(self, base):
        super().__init__(base, Berserk.name, Berserk.changing_stats)


class Blessing(AbstractPositive):
    name = "Blessing"
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

    def __init__(self, base):
        super().__init__(base, Blessing.name, Blessing.changing_stats)

from abc import ABC
from hero import Hero


class AbstractEffect(Hero, ABC):
    def __init__(self, base, name, changing_stats):
        super().__init__()
        self.base = base
        self.name = name
        self.changing_stats = changing_stats

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        current_stats = self.base.get_stats()
        for stat_key in self.changing_stats.keys():
            current_stats[stat_key] += self.changing_stats[stat_key]
        return current_stats

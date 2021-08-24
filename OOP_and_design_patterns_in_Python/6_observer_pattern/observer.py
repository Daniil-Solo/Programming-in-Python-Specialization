from abc import ABC, abstractmethod


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        title = achievement['title']
        self.achievements.add(title)
        print(self.achievements)


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, achievement):
        self.achievements.append(achievement)
        print(self.achievements)

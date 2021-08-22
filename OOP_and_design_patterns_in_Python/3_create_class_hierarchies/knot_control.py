from knot import Knot


class KnotController:
    def __init__(self, screen_dim):
        self.screen_dim = screen_dim
        self.knots = [Knot(self.screen_dim)]
        self.current = 0
        self.remove_knots = []

    def add_new(self):
        """Функция добавления новой фигуры"""
        self.remove_empty_knots()
        self.knots.append(Knot(self.screen_dim))

    def remove_empty_knots(self):
        """функция удаления фигур без точек"""
        for knot in self.knots:
            if not len(knot.points):
                self.remove_knots.append(knot)
        for knot in self.remove_knots:
            self.knots.remove(knot)
        self.remove_knots = []

    def current_knot(self):
        """функция удаления фигур без точек"""
        return self.knots[-1]

    def reset(self):
        """Удаление всех фигур с поля"""
        self.knots = [Knot(self.screen_dim)]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.knots):
            knot = self.knots[self.current]
            self.current += 1
            return knot
        else:
            self.current = 0
            raise StopIteration

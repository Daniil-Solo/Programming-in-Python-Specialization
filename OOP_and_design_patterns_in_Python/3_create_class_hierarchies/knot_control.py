from knot import Knot


class KnotController:
    def __init__(self, screen_dim):
        self.screen_dim = screen_dim
        self.knots = [Knot(self.screen_dim)]
        self.current = 0

    def add_new(self):
        self.knots.append(Knot(self.screen_dim))

    def current_knot(self):
        return self.knots[-1]

    def reset(self):
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

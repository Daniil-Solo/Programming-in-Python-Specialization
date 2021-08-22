import math
from base_class import Base


class A(Base):
    def __init__(self, data, result):
        super().__init__(data, result)
        self.loss_function = lambda x, y: (x - y) * (x - y)

    def get_score(self):
        ans = self.get_answer()
        return sum([int(x == y) for (x, y) in zip(ans, self.result)]) / len(ans)


class B(Base):
    def __init__(self, data, result):
        super().__init__(data, result)
        self.loss_function = lambda x, y: -(y * math.log(x) + (1 - y) * math.log(1 - x))

    def get_pre(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans, self.result)]
        return sum(res) / sum(ans)

    def get_rec(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans, self.result)]
        return sum(res) / sum(self.result)

    def get_score(self):
        pre = self.get_pre()
        rec = self.get_rec()
        return 2 * pre * rec / (pre + rec)


class C(Base):
    def __init__(self, data, result):
        super().__init__(data, result)
        self.loss_function = lambda x, y: abs(x - y)

    def get_score(self):
        ans = self.get_answer()
        return sum([int(x == y) for (x, y) in zip(ans, self.result)]) / len(ans)

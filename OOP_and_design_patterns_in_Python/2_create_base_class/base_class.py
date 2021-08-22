class Base:
    def __init__(self, data, result):
        self.data = data
        self.result = result
        self.loss_function = None

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_loss(self):
        return sum([self.loss_function(x, y) for (x, y) in zip(self.data, self.result)])

    def get_score(self):
        pass

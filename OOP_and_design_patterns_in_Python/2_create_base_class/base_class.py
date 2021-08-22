from abc import ABC, abstractmethod
from contracts import contract


class Base(ABC):
    @contract
    def __init__(self, data, result):
        """ Initial method
            :type data: list[>0]
            :type result: list[>0]
        """
        self.data = data
        self.result = result
        self.loss_function = None

    @contract
    def get_answer(self):
        """ Get answer
            :rtype: list[>0]
        """
        return [int(x >= 0.5) for x in self.data]

    @contract
    def get_loss(self):
        """ Get loss-value
            :rtype: float
        """
        return sum([self.loss_function(x, y) for (x, y) in zip(self.data, self.result)])

    @contract
    @abstractmethod
    def get_score(self):
        """ Get loss-value
            :rtype: float
        """
        pass

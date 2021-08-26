class BaseEvent:
    def __init__(self, value_or_type):
        self.value_or_type = value_or_type


class EventSet(BaseEvent):
    def __init__(self, value):
        super().__init__(value)


class EventGet(BaseEvent):
    def __init__(self, type_):
        super().__init__(type_)

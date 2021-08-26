class BaseEvent:
    def __init__(self, value_or_type):
        self.value_or_type = value_or_type


class SetEvent(BaseEvent):
    def __init__(self, value):
        super().__init__(value)


class GetEvent(BaseEvent):
    def __init__(self, type_):
        super().__init__(type_)

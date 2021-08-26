from events import SetEvent, GetEvent


class NullHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, obj, event):
        if not self.next_handler:
            self.next_handler.hanle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, SetEvent) and type(event.value_or_type) is int:
            obj.integer_field = event.value_or_type
        elif isinstance(event, GetEvent) and event.value_or_type is int:
            return event.value_or_type
        else:
            super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, SetEvent) and type(event.value_or_type) is float:
            obj.float_field = event.value_or_type
        elif isinstance(event, GetEvent) and event.value_or_type is float:
            return event.value_or_type
        else:
            super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, SetEvent) and type(event.value_or_type) is str:
            obj.string_field = event.value_or_type
        elif isinstance(event, GetEvent) and event.value_or_type is str:
            return event.value_or_type
        else:
            super().handle(obj, event)

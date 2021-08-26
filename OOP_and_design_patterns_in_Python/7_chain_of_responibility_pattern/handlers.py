from events import EventSet, EventGet


class NullHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, obj, event):
        if self.next_handler is not None:
            return self.next_handler.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventSet) and type(event.value_or_type) is int:
            obj.integer_field = event.value_or_type
        elif isinstance(event, EventGet) and event.value_or_type is int:
            return obj.integer_field
        else:
            # print("Передаю на выполнение ", type(self.next_handler))
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventSet) and type(event.value_or_type) is float:
            obj.float_field = event.value_or_type
        elif isinstance(event, EventGet) and event.value_or_type is float:
            return obj.float_field
        else:
            # print("Передаю на выполнение ", type(self.next_handler))
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventSet) and type(event.value_or_type) is str:
            obj.string_field = event.value_or_type
        elif isinstance(event, EventGet) and event.value_or_type is str:
            return obj.string_field
        else:
            # print("Передаю на выполнение ", type(self.next_handler))
            return super().handle(obj, event)

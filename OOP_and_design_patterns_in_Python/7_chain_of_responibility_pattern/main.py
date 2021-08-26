from some_object import SomeObject
from events import EventGet, EventSet
from handlers import FloatHandler, StrHandler, IntHandler, NullHandler


if __name__ == "__main__":

    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
    obj = SomeObject()

    chain.handle(obj, EventSet(100))
    chain.handle(obj, EventSet(3.14))
    chain.handle(obj, EventSet("aaa"))

    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))

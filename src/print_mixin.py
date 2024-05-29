class PrintMixin:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        goods = ', '.join([f"{good}={getattr(self, good)}" for good in self.__dict__])
        return f"{self.__class__.__name__}({goods})"

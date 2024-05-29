from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, prod_dict):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

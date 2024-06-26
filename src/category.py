from src.products import Product

class Category:
    name = str
    description = str
    product = list
    total_categories = 0
    counter_product = 0

    def __init__(self, name: str, description: str, product: list):
        self.name = name
        self.description = description
        self.__products = product

        Category.total_categories += 1
        Category.counter_product += len(product)

    def add_product(self, product):
        if product.quantity == 0:
            raise ValueError('Количество добавляемого товара не может быть нулевым!')
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Нельзя к продукту добавлять незнакомые объекты!")

    def calculate_price(self):
        sum_goods = 0
        try:
            for total_price in self.__products:
                sum_goods += total_price.price
            result = sum_goods / len(self.__products)
            return result
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += str(product) + '\n'
        return products_str

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        summ = 0
        for prod in self.__products:
            summ += prod.quantity
        return summ

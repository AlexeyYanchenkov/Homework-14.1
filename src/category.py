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
        self.__products.append(product)
        Category.counter_product += 1

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

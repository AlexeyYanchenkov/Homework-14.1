from src.category import Category
from src.products import Product
from src.smartphones import Smartphone


if __name__ == '__main__':
    category = Category('Смартфоны',
                        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                        [{
                           "name": "Samsung Galaxy S24 Ultra",
                           "description": "256GB, Черный титан, 200MP камера",
                           "price": 146990.0,
                           "quantity": 15
                        }])

name_1 = Product("Samsung Galaxy S24 Ultra",
                 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                 146990.0, 15)

print(name_1)

name_category = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",

                         [Product("Samsung Galaxy S24 Ultra",
                                  "256GB, Черный титан, 200MP камера",
                                  146990.0,
                                  15
                                  )])


print(name_category)


object_1 = Product("Samsung Galaxy S24 Ultra",
                   'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                   146990.0, 15)
object_2 = Product("55 QLED 4K",
                   "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                   89000.0, 15)
#object_3 = object_1 + object_2
#print(f"Сумма всего: {object_3}")

Samsung_Galaxy_S24_Ultra = Smartphone('Samsung Galaxy S24 Ultra', '200MP камера', 146990.0, 15, 12, "256GB", 256,
                                      "Черный титан")

print(Samsung_Galaxy_S24_Ultra)

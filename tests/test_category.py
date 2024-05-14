import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def category(product1):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    [product1])


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S24 Ultra", "256GB, Черный титан, 200MP камера", 146990.0, 15)


def test__init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category.products == "Samsung Galaxy S24 Ultra, 146990.0 руб. Остаток: 15\n"


def test_category(category, product1):
    assert Category.total_categories == 2
    assert Category.counter_product == 2
    category.add_product(product1)
    assert Category.counter_product == 3

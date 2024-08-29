import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def product2():
    return Product("notebook", 150, "This is a notebook", 500)

@pytest.fixture
def cart():
    return Cart()

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_name_validation(self):
        with pytest.raises(TypeError):
            Coffee(123)
        with pytest.raises(ValueError):
            Coffee("ab")
        coffee = Coffee("Latte")
        with pytest.raises(AttributeError):
            coffee.name = "NewName"
    
    def test_orders(self):
        cof = Coffee("TestCoffee")
        c = Customer("Test")
        o = Order(c, cof, 5.0)
        assert o in cof.orders()
    
    def test_customers(self):
        cof = Coffee("TestCoffee")
        c1 = Customer("Test1")
        c2 = Customer("Test2")
        Order(c1, cof, 5.0)
        Order(c1, cof, 6.0)
        Order(c2, cof, 4.5)
        assert len(cof.customers()) == 2
        assert c1 in cof.customers()
        assert c2 in cof.customers()
    
    def test_num_orders(self):
        cof = Coffee("TestCoffee")
        c = Customer("Test")
        assert cof.num_orders() == 0
        Order(c, cof, 5.0)
        assert cof.num_orders() == 1
    
    def test_average_price(self):
        cof = Coffee("TestCoffee")
        c = Customer("Test")
        assert cof.average_price() == 0
        Order(c, cof, 4.0)
        Order(c, cof, 6.0)
        assert cof.average_price() == 5.0
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_name_validation(self):
        with pytest.raises(TypeError):
            Customer(123)
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLongForValidation")
    
    def test_orders(self):
        c = Customer("Test")
        cof = Coffee("TestCoffee")
        o = Order(c, cof, 5.0)
        assert o in c.orders()
    
    def test_coffees(self):
        c = Customer("Test")
        cof1 = Coffee("Coffee1")
        cof2 = Coffee("Coffee2")
        Order(c, cof1, 5.0)
        Order(c, cof1, 6.0)
        Order(c, cof2, 4.5)
        assert len(c.coffees()) == 2
        assert cof1 in c.coffees()
        assert cof2 in c.coffees()
    
    def test_create_order(self):
        c = Customer("Test")
        cof = Coffee("TestCoffee")
        o = c.create_order(cof, 5.0)
        assert o in c.orders()
        assert o.coffee == cof
        assert o.price == 5.0
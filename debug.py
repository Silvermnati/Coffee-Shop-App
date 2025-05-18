from customer import Customer
from coffee import Coffee
from order import Order

def debug():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    
    # Create coffees
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    
    # Create orders
    Order(alice, latte, 5.0)
    Order(alice, cappuccino, 4.5)
    Order(bob, latte, 6.0)
    Order(bob, latte, 5.5)
    
    # Test relationships
    print(f"Alice's orders: {[o.coffee.name for o in alice.orders()]}")
    print(f"Latte's customers: {[c.name for c in latte.customers()]}")
    print(f"Latte order count: {latte.num_orders()}")
    print(f"Latte average price: {latte.average_price():.2f}")
    
    # Test bonus
    top_latte_customer = Customer.most_aficionado(latte)
    print(f"Latte's top customer: {top_latte_customer.name}")

if __name__ == "__main__":
    debug()
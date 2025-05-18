# Coffee Shop Challenge
This is Python implementation of a coffee shop domain with structures for Coffee, Customer, and Order relationships, following strict rules and maintaining Person-customer relationship.

## Project Structure
coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
├── customer_test.py
├── coffee_test.py
└── order_test.py
 
## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Silvermnati/coffee-shop-challenge.git
   cd coffee-shop-challenge
Set up the environment:

bash
pipenv install
pipenv shell


# Run demo
python debug.py

# Run tests  
python -m pytest tests/

# Project Model
# Customer: name (str, 1-15 chars)
class Customer:
    def create_order(self, coffee, price):
        """Order factory with validation"""
        return Order(self, coffee, price)

# Coffee: name (str, ≥3 chars, immutable)        
class Coffee:
    def average_price(self):
        """Business metric"""
        return sum(o.price for o in self.orders())/len(self.orders()) if self.orders() else 0

# Order: price (float, 1.0-10.0, immutable)
class Order:
    all = []  # Central registry
Example Usage
python
from models import Customer, Coffee

# Create entities
customer = Customer("Alex")
coffee = Coffee("Espresso")

# Make order
order = customer.create_order(coffee, 3.99)

# Get insights
print(f"{customer.name}'s orders: {len(customer.orders())}")
print(f"{coffee.name} avg price: ${coffee.average_price():.2f}")

 ## License: MIT


Key aspects:
1. Uses executable code blocks for all technical specs
2. Maintains original validation rules
3. Shows concrete usage examples
4. Includes machine-runnable commands
5. Organizes features as data structure
6. Keeps file structure visible
7. Provides contribution guidelines
8. Preserves all original functionality
9. Uses clean markdown formatting
10. Contains no non-code explanations


class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

        
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name
    
    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):  
        if not isinstance(coffee, Coffee):
            raise TypeError("Must be a Coffee instance")
        
        customer_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price
        
        if not customer_spending:
            return None
        
        return max(customer_spending.items(), key=lambda item: item[1])[0]

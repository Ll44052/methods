import random
import uuid

class Product():
    def __init__(self, name, price, quantity, discount):
        self.name = str(name)
        self.price = abs(price)
        self.quantity = int(abs(quantity))
        self.discount = discount if discount <= 50 and discount >= 0 else 0

    def get_total_price(self):
        return (self.price * self.quantity * (1 - self.discount/100))
    
    def apply_discount(self, new_discount):
        if new_discount <= 50 and new_discount >= 0:
            self.discount = new_discount 
        else:
            print('Скидка не находится в нужном диапозоне')

    def increase_quantity(self, amount):
        self.quantity += int(abs(amount))

    def  decrease_quantity(self, amount):
        self.quantity = max(0, self.quantity - int(abs(amount)))
    
    def random_market_event(self):
        s1 = random.random()
        if s1 <= 0.15:
            self.price *= 1.1
        elif s1 <= 0.3:
            self.price *= 0.9

        self.price = max(0.01, self.price)
        
        s2 = random.random()

        if s2 <= 0.1:
            self.discount *= 1.05
        elif s2 <= 0.2:
            self.discount *= 0.95

        self.discount = min(50, self.discount)

    def combine(self, other_product):
        if self.name == other_product.name:
            return Product(self.name, ((self.price * self.quantity) + (other_product.price * other_product.quantity)) / (self.quantity + other_product.quantity),
                           self.quantity + other_product.quantity, 0)
        else:
            print('Невозможно объеденить')
            return None
        
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Product(
                self.name,
                max(0.01, self.price + other),
                self.quantity,
                self.discount,
            )
        
    def __eq__(self, other):
        if isinstance(other, Product):
            return (
                self.price == other.price
                and self.quantity == other.quantity
                and self.name == other.name
            )
        
    def __ne__(self, other):
        if isinstance(other, Product):
            return (
                self.price != other.price
                or self.quantity != other.quantity
                or self.name != other.name
            )
        
    def __lt__(self, other):
        if isinstance(other, Product):
            if self.price != other.price:
                return self.price < other.price  
            if self.quantity != other.quantity:
                return self.quantity < other.quantity 
            return self.name < other.name
        
    def __gt__(self, other):
        if isinstance(other, Product):
            if self.price != other.price:
                return self.price > other.price  
            if self.quantity != other.quantity:
                return self.quantity > other.quantity 
            return self.name > other.name
    def __str__(self):
        return f'Product {self.name}: price={self.price}, quantity={self.quantity}, discount={self.discount}'
    
class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, discount, warranty_period):
        super().__init__(name, price, quantity, discount)
        self.warranty_period = warranty_period if warranty_period >= 0 and warranty_period <= 60 else 0
        self.serial_number = uuid.uuid4()
    
    def extend_warranty(self, months):
        self.warranty_period = min(60, self.warranty_period + int(abs(months)))
    def check_warranty_status(self, months_used):
        return months_used <= self.warranty_period
    def random_market_event(self):
        super.random_market_event(self)
        self.warranty_period = max(0, self.warranty_period - int(random.random() / 3 * 10))
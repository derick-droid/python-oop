"""
class and static method
"""

import csv

class Item:
    # creating a class attribute
    pay_rate = 0.85  # discount after 20%
    all_commodities = []

    # creating a constructor and creating attributes inside a constructor
    def __repr__(self):
        return f" Item ('{self.name}, {self.price}, {self.quantity}')"

    def __init__(self, name: str, price: int, quantity: int = 0):  # converting attributes into appropriate datatype
        # run validation of the received arguments
        assert price >= 0, f" {price} given is not equal or grater than zero"
        assert quantity >= 0, f"{quantity} given is not equal or greater than zero"
        # attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # assembling all commodities in one shelf
        self.all_commodities.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def discount_pay(self):
        if self.price > 35:
            self.price = self.price * self.pay_rate
        return self.price

    # creating class method
    @classmethod
    def instance_from_csv(cls):
        with open("item.csv", "r") as data:
            reader = csv.DictReader(data)
            new_list = list(reader)

        for values in new_list:
            print(values)

            # creating instances
            Item(
                name=values.get('name'),
                price=float(values.get('price')),
                quantity=int(values.get('quantity'))
            )

    # creating a static method
    @staticmethod
    def look_integer(num):  # checking for integer
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


print(Item.look_integer(7.5))
Item.instance_from_csv()
print(Item.all_commodities)



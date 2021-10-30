"""
constructor in oop
"""


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



item1 = Item("Phone", 4000, 12)  # creating an instance of a class
next_item = Item("Laptop", 2000, 12)

print(item1.calculate_total_price())
print(next_item.calculate_total_price())
# using the magic attribute to identify all the attributes in a class
print()
print(Item.__dict__)
print(item1.__dict__)
print(next_item.__dict__)
print()
print(Item.pay_rate)

# printing the price after discount
print(item1.discount_pay())
next_item.pay_rate = 0.75
print(next_item.discount_pay())

# if any case of many items

commodity1 = Item("cables", 35, 3)
commodity2 = Item("radio", 400, 9)
commodity3 = Item("switch", 90, 2)
commodity4 = Item("motor", 25, 5)
commodity5 = Item("engine", 489, 3)

# instead of magic method
for commodity in Item.all_commodities:
    print(commodity.name)
    print()
    print(commodity.price)
    print()
    print(commodity.quantity)

# while using the magic method
for commodity in Item.all_commodities:
    print(Item.all_commodities)
    
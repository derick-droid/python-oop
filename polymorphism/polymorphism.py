"""
polymorphism
"""
from item import Item
from phone import Phone
from keyboard import Keyboard
Item.instance_from_csv()
print(Item.all_commodities)
keyboard1 = Keyboard("classical", 34, 5)
print(keyboard1.name)

# polymorphism
print(keyboard1.calculate_total_price())
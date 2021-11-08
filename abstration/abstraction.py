"""
abstraction
"""
from item import Item
from phone import Phone
item1 = Item("infinix", 23)
item1.name = "Tecno"
Item.instance_from_csv()
print(Item.all_commodities)
print(item1.name)
print(item1.price)
# abstraction

item1.send_email()

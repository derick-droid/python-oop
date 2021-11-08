"""
getters and setters
"""
from item import Item
from phone import Phone
item1 = Item("infinix", 23)
item1.name = "Tecno"
Item.instance_from_csv()
print(Item.all_commodities)
print(item1.name)


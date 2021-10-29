"introduction to class"

# creating a class


class Item:

    def calculate_total_price(self, quantity, price):
        return quantity * price


item1 = Item()  # creating an instance of a class

# assigning attributes to instances
item1.name = "Phone"
item1.price = 440
item1.quantity = 4

print(item1.calculate_total_price(item1.quantity, item1.price))

next_item = Item()
next_item.price = 2000
next_item.quantity = 3
next_item.name = "Laptop"

print(next_item.calculate_total_price(next_item.price, next_item.quantity))

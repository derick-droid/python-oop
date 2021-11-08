from item import Item


class Keyboard(Item):
    # creating a constructor and creating attributes inside a constructor
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.__price}, {self.quantity}')"

    # converting attributes into appropriate datatype
    def __init__(self, name: str, price: int, quantity: int = 0,):
        # call the super function
        super().__init__(
            name, price, quantity
        )



keyboard1 = Item("classical", 45, 3)

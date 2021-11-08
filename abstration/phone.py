from item import Item


class Phone(Item):
    # creating a constructor and creating attributes inside a constructor
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.__price}, {self.quantity}')"

    # converting attributes into appropriate datatype
    def __init__(self, name: str, price: int, quantity: int = 0, broken_phone = 0):
        # call the super function
        super().__init__(
            name, price, quantity
        )
        # run validation of the received arguments
        assert broken_phone >= 0, f"{broken_phone} given is not equal or greater than zero"

phone1 = Item("infix", 45, 3)
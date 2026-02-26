class Item:
    """ЗАДАЧА: Сравнение товаров по цене через __lt__ и по всем полям через __eq__"""
    def __init__(self, name, price): self.name, self.price = name, price
    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented

        if self.price <= other.price:

            return True
        else:
            return False
    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        if self.name == other.name:
            return True
        else:
            return False
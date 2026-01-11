import json

class JsonSerializableMixin:
    """Domieszka dodająca możliwość serializacji do JSON."""
    __slots__ = ()

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)


class Product(JsonSerializableMixin):
    def __init__(self, id, price, name):
        self.id = id
        self.price = price
        self.name = name


if __name__ == '__main__':
    p = Product("SKU-1", 12.50, "Kabel USB")
    print(p.to_json())
    input("\nAby zakończyć, Enter")

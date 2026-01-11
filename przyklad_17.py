# przykład 17: AutoReprMixin

class AutoReprMixin:
    """Domieszka generująca __repr__ na podstawie atrybutów instancji."""
    __slots__ = ()

    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{type(self).__name__}({attrs})"


# Klasy korzystające z domieszki

class User(AutoReprMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Product(AutoReprMixin):
    def __init__(self, id, price, tags):
        self.id = id
        self.price = price
        self.tags = tags


if __name__ == '__main__':
    u = User("Anna", 30)
    p = Product("SKU123", 12.50, ["electronics", "sale"])

    print(u)
    print(p)


    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

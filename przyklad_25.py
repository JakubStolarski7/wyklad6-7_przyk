# deskryptor
class Quantity:
    """
    Prosty deskryptor walidujący wartość dodatnią.
    Wersja rozszerzona: obsługuje zarówno odczyt z instancji,
    jak i odczyt z klasy (Item.weight -> zwraca deskryptor).
    """

    def __init__(self, storage_name):
        # storage_name – nazwa atrybutu przechowywania w instancji zarządzanej
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("wartość musi być większa od zera!")

    def __get__(self, instance, owner):
        """
        Wywoływana przy odczycie:
            instance.attr       -> instance != None
            owner.attr          -> instance is None

        Standardowa praktyka:
        - jeśli instance is None -> zwracamy deskryptor (self)
          pozwala to na introspekcję i zachowanie zgodne z API Pythona.
        - w przeciwnym razie zwracamy wartość przechowywania.
        """
        if instance is None:
            return self       # odczyt przez klasę: Item.weight
        return instance.__dict__[self.storage_name]


# klasa zarządzana
class Item:
    # instancje deskryptora -> atrybuty zarządzane
    # 'weight' i 'price' -> atrybuty przechowywania
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description   # zwykły atrybut
        self.weight = weight             # wywołuje Quantity.__set__
        self.price = price               # wywołuje Quantity.__set__

    def total(self):
        return self.weight * self.price


if __name__ == '__main__':
    rekord = Item('cukier', 10, 30)

    print("(rekord.weight, rekord.price) ->",
          (rekord.weight, rekord.price))

    # wartości przechowywania są w __dict__
    print(f"{rekord.__dict__ = }")

    print(f"{rekord.total() = }")

    # Odczyt przez klasę -> dostajemy deskryptor
    print(f"{Item.weight = }")

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

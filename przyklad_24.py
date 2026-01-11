# deskryptor
class Quantity:
    """Prosty deskryptor walidujący wartość dodatnią."""

    def __init__(self, storage_name):
        # storage_name – nazwa atrybutu przechowywania w instancji zarządzanej
        self.storage_name = storage_name

    def __set__(self, instance, value):
        """
        Wywoływana przy przypisaniu:
        instance.attr = value
        """
        if value > 0:
            # Bezpośredni zapis do __dict__ -> unikamy rekurencji
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("wartość musi być większa od zera!")

    def __get__(self, instance, owner):
        """
        Wywoływana przy pobieraniu atrybutu:
        instance.attr  albo  owner.attr
        W tej wersji nie obsługujemy odczytu z klasy, czyli instance=None.
        """
        return instance.__dict__[self.storage_name]


# klasa zarządzana
class Item:
    # Weight i price to atrybuty zarządzane (deskryptory)
    # 'weight' i 'price' to nazwy atrybutów przechowywania
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description   # zwykły atrybut instancji
        self.weight = weight             # uruchamia Quantity.__set__
        self.price = price               # uruchamia Quantity.__set__

    def total(self):
        return self.weight * self.price


if __name__ == '__main__':
    rekord = Item('cukier', 10, 30)

    print("(rekord.weight, rekord.price) ->",
          (rekord.weight, rekord.price))

    # W __dict__ widzimy jedynie atrybuty przechowywania
    print(f"{vars(rekord) = }")

    print(f"{rekord.total() = }")

    print(Item.weight)


    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

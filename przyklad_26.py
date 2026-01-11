# deskryptor korzystający z __set_name__
class Quantity:
    """
    Deskryptor przechowujący dodatnie wartości.
    Dzięki metodzie __set_name__ nie trzeba przekazywać jawnie
    nazwy atrybutu przechowywania.
    """

    def __init__(self, storage_name=None):
        # storage_name może być None – zostanie uzupełnione w __set_name__
        self.storage_name = storage_name

    def __set_name__(self, owner, name):
        """
        Wywoływana podczas tworzenia klasy zarządzanej (np. Item).
        owner – klasa zarządzana
        name  – nazwa atrybutu, pod którą przypisano deskryptor
                (np. 'weight', 'price')
        """
        self.storage_name = name

    def __set__(self, instance, value):
        """
        Wywoływana przy przypisaniu:
        instance.attr = value
        """
        if value > 0:
            # zapis bezpośrednio do __dict__, aby uniknąć rekurencji
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("wartość musi być większa od zera!")

    # Uwaga:
    # W tej wersji brak __get__.
    # Python domyślnie pobiera wartość z instance.__dict__[storage_name],
    # co jest poprawne, ponieważ storage_name == nazwa atrybutu zarządzanego.
    # Odczyt przez klasę (Item.weight) zwróci instancję deskryptora.


# klasa zarządzana
class Item:
    # Dzięki __set_name__ nie trzeba podawać nazwy przechowywania!
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight     # uruchamia __set__
        self.price = price       # uruchamia __set__

    def total(self):
        return self.weight * self.price


if __name__ == '__main__':
    rekord = Item('cukier', 10, 30)

    print("(rekord.weight, rekord.price) ->",
          (rekord.weight, rekord.price))

    # W atrybutach instancji widzimy tylko wartości przechowywania
    print(f"{rekord.__dict__ = }")

    print(f"{rekord.total() = }")

    # odczyt przez klasę -> zwraca deskryptor
    print(f"{Item.weight = }")

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

import abc
# Abstrakcyjny deskryptor walidujący wartości
class Validated(abc.ABC):
    """
    Deskryptor abstrakcyjny.
    Deleguje walidację do metody validate(), którą muszą implementować podklasy.
    Obsługuje __set_name__, aby samodzielnie poznać nazwę atrybutu przechowywania.
    """

    def __init__(self, storage_name=None):
        self.storage_name = storage_name

    def __set_name__(self, owner, name):
        """
        Wywoływana przy tworzeniu klasy zarządzanej (np. Item).
        Dzięki temu deskryptor nie wymaga jawnego storage_name.
        """
        self.storage_name = name

    def __set__(self, instance, value):
        """
        Przypisanie:
            instance.attr = value
        Wywołuje validate(), po czym zapisuje wynik do __dict__ instancji.
        """
        validated_value = self.validate(instance, value)
        instance.__dict__[self.storage_name] = validated_value

    @abc.abstractmethod
    def validate(self, instance, value):
        """
        Zwraca zweryfikowaną wartość lub zgłasza ValueError.
        Musi być zaimplementowana w podklasach.
        """
        raise NotImplementedError


# ---------------------------------------------------------------------
# Konkretne deskryptory
# ---------------------------------------------------------------------
class Quantity(Validated):
    """Sprawdza, czy liczba jest większa od zera."""
    def validate(self, instance, value):
        if value > 0:
            return value
        raise ValueError("wartość musi być większa od zera!")


class NonBlank(Validated):
    """Sprawdza, czy ciąg tekstowy jest niepusty."""
    def validate(self, instance, value):
        if isinstance(value, str) and value.strip():
            return value
        raise ValueError("wartość musi być niepustym ciągiem tekstowym")



# Klasa zarządzana
class Item:
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description     # wywołuje validate()
        self.weight = weight
        self.price = price

    def total(self):
        return self.weight * self.price



if __name__ == '__main__':
    rekord = Item('cukier', 10, 30)
    print(vars(rekord))
    print("(rekord.description, rekord.weight, rekord.price) ->",
          (rekord.description, rekord.weight, rekord.price))

    # pierwsze trzy atrybuty z dir() to zwykle __class__, __delattr__, __dict__
    print(dir(rekord)[:3])

    # nazwa storage_name przypisana przez __set_name__
    print("storage_name NonBlank.description ->", Item.description.storage_name)

    # automatyczne pobieranie wartości
    print("rekord.description ->", getattr(rekord, 'description'))

    # odczyt przez klasę zwraca deskryptor
    print(f"{Item.weight = }")

    rekord.description = " "   # spowodowałoby ValueError

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

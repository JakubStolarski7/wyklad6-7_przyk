# fabryka właściwości
def quantity(storage_name):
    """Zwraca właściwość (property) z walidacją wartości > 0.
    storage_name – nazwa klucza w instance.__dict__, pod którym
    przechowywana będzie faktyczna wartość. Jest to przykład domknięcia.
    """

    def q_getter(instance):
        # Użycie instance.__dict__ gwarantuje, że:
        # - nie wywołujemy znowu property (brak rekurencji!)
        # - pomijamy ewentualne nadpisania
        return instance.__dict__[storage_name]

    def q_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError("wartość musi być większa od zera!")

    # zwracamy obiekt property – getter i setter mają dostęp
    # do storage_name dzięki mechanizmowi domknięcia (closure)
    return property(q_getter, q_setter)


# --- alternatywna wersja fabryki (z dekoratorami @property) ---
# def quantity(storage_name):
#     @property
#     def prop(instance):
#         return instance.__dict__[storage_name]
#     @prop.setter
#     def prop(instance, value):
#         if value > 0:
#             instance.__dict__[storage_name] = value
#         else:
#             raise ValueError("wartość musi być większa od zera!")
#     return prop


class Item:
    # tworzymy dwie właściwości za pomocą jednej fabryki
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight     # setter waliduje wartość
        self.price = price

    def total(self):
        return self.weight * self.price


if __name__ == '__main__':
    rekord = Item('cukier', 10, 30)
    print("(rekord.weight, rekord.price) ->", (rekord.weight, rekord.price))

    # rekord.weight = -1   # -> ValueError

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

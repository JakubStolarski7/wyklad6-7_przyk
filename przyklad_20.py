class Item:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight      # trafia do settera właściwości
        self.price = price        # brak walidacji – przykład problemu

    def total(self):
        return self.weight * self.price

    # --- właściwość chroniąca atrybut weight przed niepoprawnymi danymi ---

    @property
    def weight(self):
        # odczyt atrybutu z przestrzeni instancji (bezpośrednio z __dict__)
        return self.__dict__['weight']

    @weight.setter
    def weight(self, value):
        # walidacja danych wejściowych
        if value > 0:
            self.__dict__['weight'] = value
        else:
            raise ValueError("wartość musi być większa od zera!")

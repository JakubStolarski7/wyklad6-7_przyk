class Item:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight      # wywoła set_weight()
        self.price = price

    def total(self):
        return self.weight * self.price

    # --- klasyczna wersja właściwości tworzona przez konstruktor property() ---

    def get_weight(self):
        # bezpośredni dostęp do __dict__ (bez wejścia w setter)
        return self.__dict__['weight']

    def set_weight(self, value):
        # walidacja – identyczna jak w przykładzie 20
        if value > 0:
            self.__dict__['weight'] = value
        else:
            raise ValueError("wartość musi być większa od zera!")

    # tutaj property powiązuje metody: fget = get_weight, fset = set_weight
    weight = property(get_weight, set_weight)

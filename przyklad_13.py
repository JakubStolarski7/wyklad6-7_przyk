class Dad:
    def __init__(self):
        self.eyes = 'blue'


class Mom:
    def __init__(self):
        self.hair = 'curly'


# ----------------- WERSJA 1: "RĘCZNA" -----------------
# Ręcznie wywołujemy oba konstruktory klas bazowych.

class Child(Dad, Mom):
    def __init__(self):
        # oba wywołania __init__ musimy napisać sami
        Dad.__init__(self)
        Mom.__init__(self)


son = Child()
print(son.eyes)  # atrybut z klasy Dad
print(son.hair)  # atrybut z klasy Mom

print('-' * 100)

# ----------------- WERSJA 2: Z super() -----------------
# Teraz próbujemy "uprościć" inicjalizację i użyć super().

class Child(Dad, Mom):
    def __init__(self):
        # super().__init__() wywoła __init__ pierwszej klasy
        # w MRO, czyli Dad.__init__.
        # __init__ z klasy Mom NIE zostanie wywołany.
        super().__init__()


son = Child()
print(son.eyes)  # wciąż działa - Dad.__init__ ustawił eyes

# hair nie zostało ustawione, bo Mom.__init__ nie zostało wywołane,
# więc poniższa linia spowoduje AttributeError.
try:
    print(son.hair)
except AttributeError as err:
    print('Błąd przy son.hair ->', err)

# Sprawdźmy MRO, żeby zobaczyć kolejność baz:
print(Child.mro())

# help(Child) też pokazuje MRO oraz informacje o klasie:
print(help(Child))

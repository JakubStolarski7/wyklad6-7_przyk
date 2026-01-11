class Dad:
    def __init__(self):
        # wywołujemy __init__ kolejnej klasy w MRO
        super().__init__()
        self.eyes = 'blue'


class Mom:
    def __init__(self):
        # ponownie super().__init__ - tym razem z klasy Mom
        super().__init__()
        self.hair = 'curly'


class Child(Dad, Mom):
    # brak własnego __init__
    # Python użyje __init__ z pierwszej klasy w MRO, czyli Dad
    # i cała inicjalizacja "przepłynie" dalej dzięki super()
    pass
    # równoważnie moglibyśmy jawnie napisać:
    # def __init__(self):
    #     super().__init__()


son = Child()
print(son.eyes)  # atrybut ustawiony w Dad.__init__
print(son.hair)  # atrybut ustawiony w Mom.__init__

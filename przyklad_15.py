class Dad:
    def __init__(self, *args, **kwargs):
        # przekazujemy dalej wszystkie argumenty zgodnie z MRO
        super().__init__(*args, **kwargs)
        self.eyes = 'blue'


class Mom:
    def __init__(self, hair, *args, **kwargs):
        # najpierw wywołujemy kolejną klasę w MRO,
        # a dopiero potem ustawiamy własne atrybuty
        super().__init__(*args, **kwargs)
        self.hair = hair


class Child(Dad, Mom):
    def __init__(self, *args, **kwargs):
        # jedno wywołanie super().__init__() uruchamia całą "kaskadę"
        # zgodnie z MRO: Child -> Dad -> Mom -> object
        super().__init__(*args, **kwargs)


son = Child("curly")
print(son.eyes)   # ustawione w Dad.__init__
print(son.hair)   # ustawione w Mom.__init__

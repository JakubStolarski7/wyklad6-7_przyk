class Dad:
    def __init__(self):
        # atrybut ustawiany przez ojca
        self.eyes = 'blue'


class Mom:
    def __init__(self):
        # atrybut ustawiany przez matkę
        self.hair = 'curly'


class Child(Dad, Mom):
    # brak własnego __init__
    # Python użyje __init__ pierwszej klasy w MRO, czyli Dad
    pass


# tworzymy obiekt Child
son = Child()

# atrybut z klasy Dad
print(son.eyes)


# atrybut z klasy Mom - UWAGA:
# tu zadziała zasada: "czytam atrybuty po MRO",
print(son.hair)




# proste wywoływanie metody klasy bazowej
class A:
    def method(self):
        print('A.method()')


class B(A):
    def method(self):
        print('B.method()')
        # wywołujemy wersję metody z klasy bazowej A
        super().method()


if __name__ == '__main__':
    b = B()
    b.method()
    print('--' * 30)


# funkcja super() w metodzie __init__() - kontrola nad inicjalizacją
# elementów klasy bazowej

class C:
    def __init__(self):
        self.x = 0


class D(C):
    def __init__(self):
        # inicjalizujemy część z klasy C
        super().__init__()
        # a dopiero potem rozszerzamy o własne atrybuty
        self.y = 1


if __name__ == '__main__':
    d = D()
    print("d.x ->", d.x)
    print("d.y ->", d.y)
    print('--' * 30)


# funkcja super() w kodzie przesłaniającym metody specjalne Pythona
class Exchange:
    def __init__(self, item):
        # UWAGA: tu wywołujemy __setattr__!
        # musimy użyć super(), żeby nie wpaść w nieskończoną rekursję
        super().__setattr__('_item', item)


    def __getattr__(self, name):
        # gdy atrybut nie zostanie znaleziony w Exchange,
        # delegujemy odczyt do obiektu opakowywanego (_item)
        return getattr(self._item, name)

    def __setattr__(self, name, value):
        # atrybuty zaczynające się od '_' zapisujemy w Exchange
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            # pozostałe atrybuty zapisujemy w opakowywanym obiekcie
            setattr(self._item, name, value)


class E:
    def __init__(self):
        self.x = 1
        self._y = 2


if __name__ == '__main__':
    e = E()
    z = Exchange(e)

    print("e.__dict__ ->", vars(e))
    print("z.__dict__ ->", vars(z))

    print("z.x ->", z.x)  # delegacja do e.x

    # z.__dict__['xx'] = 13
    z.xx = 3      # trafi do e.xx
    z.yy = 4      # trafi do e.yy
    z._xx = 5     # trafi do z.__dict__['_xx']

    print("z.xx ->", z.xx)
    print("z.yy ->", z.yy)
    print("z._xx ->", z._xx)

    print("e.__dict__ ->", vars(e))  # tu widać xx i yy
    print("z.__dict__ ->", vars(z))  # tu widać _item i _xx

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

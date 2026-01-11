# ------------------ WERSJA "RĘCZNA" – BEZ super() ------------------

class A:
    def __init__(self):
        print('A.__init__()')


class B(A):
    def __init__(self):
        # wywołanie konstruktora A bez użycia super()
        A.__init__(self)
        print('B.__init__()')


class C(A):
    def __init__(self):
        # C również ręcznie wywołuje A.__init__
        A.__init__(self)
        print('C.__init__()')


class D(B, C):
    def __init__(self):
        # UWAGA: wywołujemy osobno B.__init__ i C.__init__
        # każdy z nich wywoła A.__init__, więc A.__init__()
        # zostanie wykonane DWUKROTNIE
        B.__init__(self)
        C.__init__(self)
        print('D.__init__()')


if __name__ == '__main__':
    print('Tworzymy D() - wersja bez super():')
    D()
    print('--' * 30)
    print('Kolejność wywoływania metod klasy D - atrybut __mro__')
    print('D.__mro__ ->', D.__mro__)
    print('--' * 30)



# ------------------ WERSJA POPRAWNA – z użyciem super() ------------------

class A1:
    def __init__(self):
        print('A1.__init__()')


class B1(A1):
    def __init__(self):
        # korzystamy z super() - przekazujemy wywołanie dalej zgodnie z MRO
        super().__init__()
        print('B1.__init__()')


class C1(A1):
    def __init__(self):
        # ponownie super() - MRO zadba, aby A1.__init__ został wywołany raz
        super().__init__()
        print('C1.__init__()')


class D1(B1, C1):
    def __init__(self):
        # jedno wywołanie super().__init__() uruchomi całą "kaskadę"
        # wywołań __init__ według MRO: D1 -> B1 -> C1 -> A1 -> object
        super().__init__()
        print('D1.__init__()')


if __name__ == '__main__':
    print('Tworzymy D1() - wersja z super():')
    D1()
    print('--' * 30)
    print('Kolejność wywoływania metod klasy D1 - atrybut __mro__')
    from pprint import pprint
    print('D1.mro() ->', end=" ")
    pprint(D1.mro())
    print('--' * 30)

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

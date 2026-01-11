class A:
    def f(self):
        print('Af', self)


class B(A):
    def g(self):
        print('Bg', self)


class C(A):
    def g(self):
        print('Cg', self)


class D(B, C):
    def f(self):
        # super().f() - szuka f według MRO:
        # D -> B -> C -> A -> object
        # f znajduje dopiero w A, więc wywoła A.f(self)
        super().f()
        print('Df', self)

    def fg(self):
        # self.f() - korzysta z D.f (czyli najpierw A.f przez super(), potem Df)
        self.f()

        # super().f() - wywołuje f z kolejnej klasy w MRO po D, czyli z A
        super().f()

        # self.g() - szuka g po MRO: D -> B -> C -> A -> ...
        # pierwsze g jest w B, więc wywoła B.g(self)
        self.g()

        # super().g() - startuje szukanie g za D w MRO,
        # więc znów trafi na B.g(self)
        super().g()

        # C.g(self) - jawne wywołanie metody z klasy C,
        # z pominięciem MRO i super()
        C.g(self)

if __name__ == '__main__':
    from pprint import pprint

    print('--' * 30)
    print('Kolejność wywoływania metod klasy D - atrybut __mro__')

    print('D.__mro__ ->', end=' ')
    pprint(D.__mro__)   # krotka z kolejnością wyszukiwania metod

    print('D.mro() ->', end=' ')
    pprint(D.mro())     # ta sama informacja w postaci listy

    # help(D) pokazuje MRO i inne informacje o klasie,
    help(D)

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

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
    print('--' * 30)
    d = D()

    print("d.g() ->", end=' ')
    d.g()

    print("C.g(d) ->", end=' ')
    C.g(d)

    print("d.f() ->", end=' ')
    d.f()

    print('--' * 30)
    print("d.fg() ->", end=' ')
    d.fg()

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

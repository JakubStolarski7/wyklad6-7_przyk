# ------------------ PRZYPADEK 1 ------------------
# Proste, jednokrotne dziedziczenie — wywołanie konstruktora
# klasy bazowej "ręcznie" jeszcze działa poprawnie.

class A1:
    def __init__(self):
        print('A1.__init__()')


class B1(A1):
    def __init__(self):
        # UWAGA: tu wołamy konstruktor A1 bez użycia super()
        # Przy jednokrotnym dziedziczeniu to zadziała,
        # ale NIE jest to zalecana praktyka.
        A1.__init__(self)
        print('B1.__init__()')


if __name__ == '__main__':
    print('Działa!')
    B1()
    print('--' * 30)



# ------------------ PRZYPADEK 2 ------------------
# Wielodziedziczenie (diament) — brak super() powoduje duplikację wywołań.

class A:
    def __init__(self):
        print('A.__init__()')


class B(A):
    def __init__(self):
        # B wywołuje A.__init__ bez super() — to już potencjalny problem
        A.__init__(self)
        print('B.__init__()')


class C(A):
    def __init__(self):
        # C również wywołuje A.__init__ bez super()
        A.__init__(self)
        print('C.__init__()')

# MRO dla D to: (D, B, C, A, object)
# ale poniżej ignorujemy MRO i wołamy konstruktory ręcznie!

class D(B, C):
    def __init__(self):
        # UWAGA — OTO KLUCZOWY BŁĄD:
        # Wywołując B.__init__ i C.__init__ oddzielnie,
        # wywołamy A.__init__() DWUKROTNIE!!!
        B.__init__(self)
        C.__init__(self)
        print('D.__init__()')


if __name__ == '__main__':
    print('Ale?')
    d = D()

    # Problem: konstruktor A został wywołany dwa razy.
    # Dlatego w wielodziedziczeniu należy stosować super()
    # zamiast wywoływać konstruktory klas bazowych „ręcznie”.

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

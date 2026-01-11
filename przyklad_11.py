class A:
    def method(self):
        print('A.method')
        # super() szuka kolejnej definicji method według MRO.
        # Dla samej klasy A MRO to: (A, object),
        # więc super().method() będzie szukało method w object
        # i spowoduje AttributeError.
        super().method()


if __name__ == '__main__':
    try:
        a = A()
        a.method()
    except AttributeError as err:
        # tutaj widzimy, że super() "nie ma dokąd pójść"
        # i zgłasza błąd
        print(err)

    print('--' * 40)


class B:
    def method(self):
        print('B.method')


class C(A, B):
    # brak własnej implementacji method - użyjemy tej z A
    # MRO dla C to: (C, A, B, object)
    # więc super().method() wywołane wewnątrz A.method
    # sięgnie dalej do B.method.
    pass


if __name__ == '__main__':
    c = C()
    c.method()

    print('--' * 40)
    from pprint import pprint
    print('C.mro() ->', end=" ")
    pprint(C.mro())

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

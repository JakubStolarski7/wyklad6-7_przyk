from module import print_arg, show


class DSetGet:
    """
    Deskryptor przesłaniający (data descriptor).
    Implementuje __get__ i __set__.
    W tym przykładzie jest tylko „dla porównania” – nie używamy go w mainie.
    """
    def __get__(self, instance, owner):
        print_arg('get', self, instance, owner)

    def __set__(self, instance, value):
        print_arg('set', self, instance, value)


class DSet:
    """
    Deskryptor nadpisujący (set-only).

    Ma tylko __set__, ale nie __get__:
    - przy zapisie: wywoływany jest __set__
    - przy odczycie: Python szuka najpierw w instancji (instance.__dict__),
      a jeśli nic tam nie ma – zwraca obiekt deskryptora z klasy.
    """
    def __set__(self, instance, value):
        # np. -> DSet.__set__(<DSet object>, <A object>, 10)
        print_arg('set', self, instance, value)


class DGet:
    """
    Deskryptor nieprzesłaniający (non-data descriptor).
    Implementuje tylko __get__.
    Może zostać nadpisany przez atrybut instancji.
    """
    def __get__(self, instance, owner):
        print_arg('get', self, instance, owner)


class A:
    d_s_g = DSetGet()
    d_s   = DSet()   # bohater tego przykładu
    d_g   = DGet()

    def method(self):
        print(f'-> A.method({show(self)})')


if __name__ == '__main__':
    # deskryptor „set-only”
    a = A()

    print("a.d_s:")
    print(a.d_s)
    # brak __get__ w DSet:
    # - instancja nie ma 'd_s' w __dict__
    # - więc odczyt zwraca obiekt deskryptora z klasy A.d_s
    # (show(...) wypisze np. <DSet object>)

    print("A.d_s:")
    print(A.d_s)   # odczyt przez klasę – też zwraca obiekt DSet

    # zapis – zawsze przez __set__ deskryptora
    a.d_s = 10      # -> DSet.__set__(...)

    print("a.d_s:")
    print(a.d_s)
    # __set__ nic nie zapisuje do instance.__dict__ – dalej widzimy deskryptor

    # Teraz nadpisujemy atrybut instancji, omijając deskryptor
    a.__dict__['d_s'] = 11
    print("vars(a):")
    print(vars(a))

    print("a.d_s:")
    print(a.d_s)
    # teraz odczyt:
    # - dla deskryptora „set-only” Python przy lookupie bierze wartość z instancji,
    #   więc dostajemy 11 (a nie obiekt DSet)

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

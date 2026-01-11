from module import print_arg, show


class DSetGet:
    """
    Deskryptor przesłaniający (data descriptor).
    W tym przykładzie jest tylko „dla kontekstu”.
    """
    def __get__(self, instance, owner):
        print_arg('get', self, instance, owner)

    def __set__(self, instance, value):
        print_arg('set', self, instance, value)


class DSet:
    """
    Deskryptor przesłaniający częściowy (set-only).
    W tym przykładzie nie jest używany w mainie.
    """
    def __set__(self, instance, value):
        print_arg('set', self, instance, value)


class DGet:
    """
    Deskryptor nieprzesłaniający (non-data descriptor).
    Implementuje tylko __get__.

    Konsekwencja:
    - odczyt atrybutu: wywołuje __get__
    - zapis atrybutu na instancji: tworzy zwykły atrybut instancji,
      który później przesłania deskryptor.
    """
    def __get__(self, instance, owner):
        # np. -> DGet.__get__(<DGet object>, <A object>, <class A>)
        print_arg('get', self, instance, owner)


class A:
    d_s_g = DSetGet()
    d_s   = DSet()
    d_g   = DGet()   # bohater tego przykładu

    def method(self):
        print(f'-> A.method({show(self)})')


if __name__ == '__main__':
    # deskryptor nieprzesłaniający
    a = A()

    print("a.d_g:")
    a.d_g             # instance != None → wywołuje DGet.__get__

    print("A.d_g:")
    A.d_g             # instance = None → wywołuje DGet.__get__ z instance=None

    # brak __set__ w deskryptorze:
    # przypisanie tworzy zwykły atrybut instancji
    a.d_g = 10        # teraz w a.__dict__ powstaje 'd_g': 10

    print("a.d_g:")
    print(a.d_g)      # odczyt korzysta już z a.__dict__['d_g'], deskryptor jest przesłonięty

    print("A.d_g:")
    A.d_g             # nadal deskryptor na poziomie klasy

    # usuwamy atrybut instancji
    del a.d_g

    print("a.d_g:")
    a.d_g             # po usunięciu atrybutu instancji znów działa deskryptor (DGet.__get__)

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

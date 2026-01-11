from module import print_arg, show


class DSetGet:
    """
    Deskryptor przesłaniający (data descriptor).
    W tym przykładzie służy tylko jako tło – nie używamy go w mainie.
    """
    def __get__(self, instance, owner):
        print_arg('get', self, instance, owner)

    def __set__(self, instance, value):
        print_arg('set', self, instance, value)


class DSet:
    """
    Deskryptor przesłaniający częściowy (set-only).
    Również tylko „dla kompletu”.
    """
    def __set__(self, instance, value):
        print_arg('set', self, instance, value)


class DGet:
    """
    Deskryptor nieprzesłaniający (non-data descriptor).
    Analogiczny do tego, jak działają zwykłe metody.
    """
    def __get__(self, instance, owner):
        print_arg('get', self, instance, owner)


class A:
    d_s_g = DSetGet()
    d_s   = DSet()
    d_g   = DGet()

    def method(self):
        print(f'-> A.method({show(self)})')


if __name__ == '__main__':
    a = A()

    # Metoda jest deskryptorem nieprzesłaniającym:
    # A.method -> funkcja (unbound function / function object)
    # a.method -> obiekt metody powiązanej z instancją
    print('a.method ->', a.method)   # bound method
    print('A.method ->', A.method)   # function

    # Przypisanie do a.method tworzy zwykły atrybut instancji
    # i przesłania deskryptor (metodę) tylko dla tej instancji.
    a.method = 7

    print('a.method ->', a.method)   # teraz zwykła wartość (7), deskryptor nie działa
    print('A.method ->', A.method)   # nadal oryginalna funkcja w klasie

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

from module import print_arg, show

class DSetGet:
    """
    Deskryptor przesłaniający (data descriptor).
    Implementuje __get__ i __set__, więc zawsze ma
    pierwszeństwo nad atrybutami instancji.
    """
    def __get__(self, instance, owner):
        # print_arg wypisuje np.:
        # -> DSetGet.__get__(<DSetGet object>, <A object>, <class A>)
        print_arg('get', self, instance, owner)

    def __set__(self, instance, value):
        # -> DSetGet.__set__(<DSetGet object>, <A object>, 10)
        print_arg('set', self, instance, value)


class DSet:
    """
    Deskryptor przesłaniający częściowy (ma __set__, ale nie __get__).
    Przy odczycie Python najpierw sprawdzi __dict__ instancji.
    """
    def __set__(self, instance, value):
        print_arg('set', self, instance, value)


class DGet:
    """
    Deskryptor nieprzesłaniający (non-data descriptor).
    Implementuje tylko __get__. Jeśli instancja zawiera atr. o tej nazwie,
    wygrywa atrybut instancji.
    """
    def __get__(self, instance, owner):
        print_arg('get', self, instance, owner)


# Klasa zarządzana
class A:
    d_s_g = DSetGet()   # deskryptor przesłaniający
    d_s   = DSet()      # deskryptor przesłaniający częściowy
    d_g   = DGet()      # deskryptor nieprzesłaniający

    def method(self):
        print(f'-> A.method({show(self)})')


# Przykłady zachowania deskryptorów

if __name__ == '__main__':
    a = A()

    print("a.d_s_g:")
    a.d_s_g                # instance != None → normalny get z instancji

    print("A.d_s_g:")
    A.d_s_g                # instance = None → odczyt przez klasę

    a.d_s_g = 10           # zapis -> __set__

    
    # Próba nadpisania deskryptora przez atrybut instancji
    a.__dict__['d_s_g'] = 11   # omijamy deskryptor przy zapisie
    print("vars(a):")
    print(vars(a))

    print("a.d_s_g:")
    a.d_s_g                # deskryptor przesłaniający nadal wygrywa

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

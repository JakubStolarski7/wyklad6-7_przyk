class A:
    atr = 'jestem atrybutem klasy'

    @property
    def prop(self):
        return "wartość właściwości"


if __name__ == '__main__':
    a = A()

    # vars zwraca __dict__ obiektu a (tylko atrybuty instancji)
    print('vars(a) ->', vars(a))

    # odczyt atrybutu klasy przez instancję (instancja nie ma własnego 'atr')
    print('a.atr ->', a.atr)

    # utworzenie atrybutu instancji 'atr'
    a.atr = 'coś'
    print('vars(a) ->', vars(a))

    # atrybut instancji przesłania atrybut klasy
    print('a.atr ->', a.atr)

    # odczyt atrybutu klasy poprzez nazwę klasy
    print('A.atr ->', A.atr)

    print('#' * 60)

    # odczytanie prop posługując się nazwą klasy zwraca obiekt właściwości (deskryptor)
    print('A.prop ->', A.prop)

    # odczyt przez instancję wywołuje metodę właściwości (fget)
    print('a.prop ->', a.prop)


    # próba ustawienia atrybutu instancji prop (brak settera -> błąd)
    print("a.prop = 'nowa wartość' ->", end=" ")
    try:
        a.prop = 'nowa wartość'
    except AttributeError as err:
        print(err)

    print('#' * 60)

    # wstawiamy 'prop' bezpośrednio do a.__dict__ (tworzymy atrybut instancji)
    a.__dict__['prop'] = 'nowa wartość'
    print('vars(a) ->', vars(a))

    # mimo a.__dict__['prop'], odczyt a.prop wciąż używa właściwości z klasy A
    print('a.prop ->', a.prop)

    # nadpisanie A.prop zwykłym atrybutem klasy niszczy obiekt właściwości
    A.prop = 'upss'
    print('a.prop ->', a.prop)   # teraz odczytujemy po prostu A.prop

    # atrybut instancji
    print('a.atr ->', a.atr)
    # atrybut klasy
    print('A.atr ->', A.atr)

    # przesłonięcie atrybutu klasy nową właściwością
    A.atr = property(lambda self: 'wartość właściwości "atr"')

    # atrybut instancji 'a.atr' zostaje przesłonięty przez właściwość z klasy
    print('a.atr ->', a.atr)

    # usuwamy właściwość z klasy
    del A.atr

    # po usunięciu właściwości znów obowiązuje atrybut instancji
    print('a.atr ->', a.atr)

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

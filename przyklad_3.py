import collections


class MyDict1(collections.UserDict):
    def __setitem__(self, key, value):
        # wywołujemy metodę klasy nadrzędnej,
        # ale zapisujemy wartość jako listę z dwoma kopiami
        super().__setitem__(key, [value] * 2)


class MyDict2(collections.UserDict):
    def __getitem__(self, key):
        # zawsze zwracamy ten sam napis, niezależnie od klucza
        return 'słowik'


if __name__ == '__main__':
    # --- MyDict1: nadpisane __setitem__ ---

    d1 = MyDict1(red='czerwony')
    print(d1)  # {'red': ['czerwony', 'czerwony']}

    d1['blue'] = 'niebieski'
    print(d1)  # 'blue' -> ['niebieski', 'niebieski']

    d1.update(black='czarny')
    print(d1)  # 'black' -> ['czarny', 'czarny']

    print('--' * 30)

    # --- MyDict2: nadpisane __getitem__ ---

    dd = MyDict2(k=1)
    print("print(d2) ->", dd)        # {'k': 1}
    print("d2['k'] ->", dd['k'])     # słowik

    d = {}
    d.update(dd)
    print("print(d) ->", d)          # {'k': 'słowik'}
    print("d['k'] ->", d['k'])       # słowik

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

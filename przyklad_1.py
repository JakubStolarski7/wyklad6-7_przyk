class MyDict1(dict):
    def __setitem__(self, key, value):
        # wywołujemy metodę klasy nadrzędnej,
        # ale zapisujemy wartość jako listę z dwoma kopiami
        super().__setitem__(key, [value] * 2)


if __name__ == '__main__':
    # konstruktor dict IGNORUJE nasze przesłonięcie __setitem__
    dd = MyDict1(red='czerwony')
    print(dd)  # {'red': 'czerwony'}

    # operator [] korzysta z nadpisanego __setitem__
    dd['blue'] = 'niebieski'
    print(dd)  # {'red': 'czerwony', 'blue': ['niebieski', 'niebieski']}

    # metoda update również IGNORUJE nasze __setitem__
    dd.update(black='czarny')
    print(dd)  # 'black' nie jest listą

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
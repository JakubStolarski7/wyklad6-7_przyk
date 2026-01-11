class MyDict2(dict):
    def __getitem__(self, key):
        # zawsze zwracamy ten sam napis, niezależnie od klucza
        return 'słowik'


if __name__ == '__main__':
    # konstruktor dict nie korzysta z __getitem__ klasy potomnej
    dd = MyDict2(k = 1)
    print("print(dd) ->", dd)     # {'k': 1}

    # operator [] korzysta z naszego __getitem__
    print("dd['k'] ->", dd['k'])  # słowik

    # update() pobiera wartości BEZ wywoływania nadpisanego __getitem__
    d = {}
    d.update(dd)
    print("print(d) ->", d)       # {'k': 1}
    print("d['k'] ->", d['k'])    # 1

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

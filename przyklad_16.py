import collections


class MappingMixin:
    """Do celów diagnostycznych"""
    __slots__ = ()
    def __getitem__(self, key):
        print(f'Pobrano: {key}')
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print(f'Ustawiono: {key} = {value}')
        super().__setitem__(key, value)

    def __delitem__(self, key):
        print(f'Usunięto {key}')
        super().__delitem__(key)


# Przykład zastosowania klasy MappingMixin

class MyDict(MappingMixin, collections.UserDict):
    pass


if __name__ == '__main__':
    d = MyDict()
    d['red'] = 'czerwony'
    print(d['red'])
    print(d)
    del d['red']
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")



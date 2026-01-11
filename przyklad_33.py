import collections


class Text(collections.UserString):
    def __repr__(self):
        return f'{self.__class__.__name__}({self.data!r})'

    def reverse(self):
        return self[::-1]

    def __str__(self):
        return repr(self)


if __name__ == '__main__':
    word = Text('kopytko')
    print(word)
    print(word.reverse())

    # metoda wywoływana na klasie działa jak zwykła funkcja
    print(Text.reverse(Text('słowik')))

    # różne typy: funkcja na klasie vs metoda powiązana z instancją
    print("type(Text.reverse), type(word.reverse) ->", end=' ')
    print(type(Text.reverse), type(word.reverse))

    # Text.reverse jako funkcja współpracująca z różnymi obiektami sekwencyjnymi
    L = list(map(Text.reverse, ['kotek', [1, 2, 3, 4], Text('młotek')]))
    print(L)

    # funkcja zdefiniowana w klasie to deskryptor nieprzesłaniający
    # wywołanie jej metody __get__ z instancją zwraca metodę powiązaną z tą instancją
    print(Text.reverse.__get__(word))

    # wywołanie __get__ z instance = None zwraca samą funkcję
    print(f"{Text.reverse.__get__(None, Text) = }")

    # word.reverse jest równoznaczne z Text.reverse.__get__(word)
    print(f"{word.reverse = }")

    # obiekt metody powiązanej ma atrybut __self__ - odwołanie do instancji,
    # dla której metoda została powiązana
    print(f"{word.reverse.__self__ = }")

    # obiekt metody powiązanej ma atrybut __func__ - odwołanie do pierwotnej
    # funkcji zdefiniowanej w klasie zarządzanej
    print(f"{word.reverse.__func__ = }")

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

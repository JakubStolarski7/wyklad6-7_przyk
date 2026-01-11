import collections.abc, collections, numbers


#-----------------------------------------------------------------
# Prosta implementacja talii kart jako klasy dziedziczącej
# po abstrakcyjnej klasie MutableSequence.

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck2(collections.abc.MutableSequence):
    # rangi kart: 2-10 + figury
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # kolory kart
    suits = 'kier karo trefl pik'.split()

    def __init__(self):
        # tworzymy pełną talię kart jako listę namedtuple
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    # poniżej implementujemy metody wymagane przez MutableSequence

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)


#------------------------------------------------------------------

def print_mro(cls):
    """Pomocnicza funkcja wypisująca MRO (kolejność przeszukiwania metod)."""
    for c in cls.__mro__:
        print(c.__name__)


if __name__ == '__main__':
    print("---bool---")
    # MRO typu bool (dziedziczy po int)
    print_mro(bool)

    print("---Deck2---")
    # MRO naszej klasy Deck2 (MutableSequence, Sequence, Sized, itp.)
    print_mro(Deck2)

    print("---collections.abc.Mapping---")
    # MRO abstrakcyjnej klasy mapującej
    print_mro(collections.abc.Mapping)

    print("---numbers.Rational---")
    # MRO dla typu "liczba wymierna" z modułu numbers
    print_mro(numbers.Rational)

    print("---ZeroDivisionError---")
    # MRO dla wyjątku ZeroDivisionError (hierarchia wyjątków)
    print_mro(ZeroDivisionError)

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

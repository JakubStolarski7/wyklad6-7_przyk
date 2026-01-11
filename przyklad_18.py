class ComparableMixin:
    """Domieszka dodająca standardowe operatory porównania."""
    __slots__ = ()

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

class Person(ComparableMixin):
    def __init__(self, age):
        self.age = age

    # wymagane przez ComparableMixin:
    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age


if __name__ == '__main__':
    p1 = Person(25)
    p2 = Person(30)

    print(p1 < p2)
    print(p1 >= p2)
    print(p1 == p2)
    input("\nAby zakończyć, Enter")

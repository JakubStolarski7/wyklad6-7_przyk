def conjunction(*obiekty):
    return FuzzyBool(min(obiekty))


def disjunction(*obiekty):
    return FuzzyBool(max(obiekty))


class FuzzyBool(float):
    # własna metoda __new__() gwarantuje niezmienność tworzonego obiektu
    # i przycina wartość do przedziału [0.0, 1.0]
    def __new__(cls, value=0.0):
        return super().__new__(cls, value if 0.0 <= value <= 1.0 else 0.0)

    def __invert__(self):
        # negacja rozmyta: 1 - x
        return FuzzyBool(1.0 - float(self))

    def __and__(self, other):
        # koniunkcja rozmyta: min(x, y)
        return FuzzyBool(min(self, other))

    def __iand__(self, other):
        return FuzzyBool(min(self, other))

    def __or__(self, other):
        # alternatywa rozmyta: max(x, y)
        return FuzzyBool(max(self, other))

    def __ior__(self, other):
        return FuzzyBool(max(self, other))

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"

    def __bool__(self):
        # wartość logiczna: prawda, jeśli stopień prawdziwości > 0.5
        return self > 0.5

    def __int__(self):
        return round(self)

    # funkcja exec(instrukcje) — jeżeli argument jest ciągiem tekstowym,
    # to jest on parsowany jako ciąg instrukcji Pythona i wykonywany
    # (o ile jest wolny od błędów składniowych).

    # --- wyłączamy niechciane operatory jednoargumentowe ---
    for name, operator in (("__neg__", "-"),):
        # komunikat błędu z wstawionym operatorem (np. "-")
        text = (
            f"nieprawidłowy typ operandu dla operacji jednoargumentowej {operator}: "
            "'{self}'"
        )

        # budujemy definicję funkcji jako kod źródłowy
        exec(
            f"def {name}(self):\n"
            f"    raise TypeError(\"{text}\".format(self=self.__class__.__name__))"
        )

    # --- wyłączamy hurtowo operatory dwuargumentowe ---
    for name, operator in (
            ("__xor__", "^"), ("__ixor__", "^="),
            ("__add__", "+"), ("__iadd__", "+="), ("__radd__", "+"),
            ("__sub__", "-"), ("__isub__", "-="), ("__rsub__", "-"),
            ("__mul__", "*"), ("__imul__", "*="), ("__rmul__", "*"),
            ("__pow__", "**"), ("__ipow__", "**="), ("__rpow__", "**"),
            ("__floordiv__", "//"), ("__ifloordiv__", "//="), ("__rfloordiv__", "//"),
            ("__truediv__", "/"), ("__itruediv__", "/="), ("__rtruediv__", "/"),
            ("__divmod__", "divmod()"), ("__rdivmod__", "divmod()"),
            ("__mod__", "%"), ("__imod__", "%="), ("__rmod__", "%"),
            ("__lshift__", "<<"), ("__ilshift__", "<<="), ("__rlshift__", "<<"),
            ("__rshift__", ">>"), ("__irshift__", ">>="), ("__rrshift__", ">>"),):
        # tekst komunikatu z operatorem, z placeholderami {self}, {join}, {args}
        text = (
            f"nieobsługiwany typ(y) operandu dla {operator}: "
            "'{self}'{join} {args}"
        )

        exec(
            f"def {name}(self, *args):\n"
            f"    operands = [\"'\" + arg.__class__.__name__ + \"'\" for arg in args]\n"
            f"    raise TypeError(\n"
            f"        \"{text}\".format(\n"
            f"            self=type(self).__name__,\n"
            f"            join=(\" and\" if len(args) == 1 else \",\"),\n"
            f"            args=\", \".join(operands)\n"
            f"        )\n"
            f"    )"
        )


if __name__ == '__main__':
    FuzzyBool.conjunction = conjunction
    FuzzyBool.disjunction = disjunction

    r1 = FuzzyBool(0.2)
    r2 = FuzzyBool(0.6)
    r3 = FuzzyBool(7)  # zostanie przycięty do 0.0
    print('r1 ->', r1)
    print('r2 ->', r2)
    print('r3 ->', r3)
    print('~r1 ->', ~r1)
    print('r1 | r2 ->', r1 | r2)
    print('r1 & r2 ->', r1 & r2)
    print('FuzzyBool.conjunction(r1, r2, r3) ->',
          FuzzyBool.conjunction(r1, r2, r3))
    print('FuzzyBool.disjunction(r1, r2, r3) ->',
          FuzzyBool.disjunction(r1, r2, r3))


    # poniższa linia spowoduje TypeError, bo + jest "wyłączone"
    print(r1 + r2)


    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

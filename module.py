############################################################################
# Funkcje pomocnicze do wizualizacji wywołań deskryptorów
############################################################################

def class_name(ob_or_cls):
    """
    Zwraca nazwę klasy:
    - dla obiektu → jego type.__name__
    - dla klasy   → class.__name__
    """
    cls = type(ob_or_cls)
    if cls is type:      # ob_or_cls jest klasą
        cls = ob_or_cls
    return cls.__name__.split(".")[-1]


def show(ob):
    """
    Zwraca czytelne przedstawienie obiektów przekazywanych
    do deskryptorów (__get__, __set__).
    """
    cls = type(ob)

    if cls is type:
        return f"<class {ob.__name__}>"   # np. <class A>
    elif cls in [type(None), int]:
        return repr(ob)                   # None, 10, 5 itd.
    else:
        return f"<{class_name(ob)} object>"


def print_arg(name, *args):
    """
    Wypisuje wywołanie deskryptora w formacie:
    -> DSetGet.__get__(<DSetGet object>, <A object>, <class A>)
    """
    printable = ", ".join(show(a) for a in args)
    print(f"-> {class_name(args[0])}.__{name}__({printable})")


############################################################################
if __name__ == "__main__":
    print("To jest moduł i powinien być importowany!")


def ejercicio1(lista):
    lista = ["P", "t"]
    lista.remove("t")
    lista.append("ython")
    # TO DO
    assert "".join(lista) == "Python"


def ejercicio2():
    lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
    lista[:-5]
    del lista[-2]
    lista.sort()
    assert lista == list(range(1, 6))

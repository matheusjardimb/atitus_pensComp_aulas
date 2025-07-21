def letra_comum(lista: list) -> str:
    pass


def test():
    assert letra_comum(["banana", "abacate", "hi", "eeeeeeeeeeeeeeeeeeeeeee"]) == "e"
    assert letra_comum(["banana", "abacate"]) == "a"
    assert letra_comum([]) == ""
    assert letra_comum([""]) == ""
    assert letra_comum(["abc"]) == ""
    assert letra_comum(["a"]) == "a"

# https://leetcode.com/problems/longest-common-prefix/description/
def longest_common_prefix(lista_palavras: list[str]) -> str:
    pass


def test():
    assert longest_common_prefix([]) == ""
    assert longest_common_prefix([""]) == ""
    assert longest_common_prefix(["dog"]) == "dog"
    assert longest_common_prefix(["dog", "dogs"]) == "dog"
    assert longest_common_prefix(["dogs", "dog"]) == "dog"
    assert longest_common_prefix(["dog", "dog", "dog"]) == "dog"
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "door", "disc"]) == "d"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""

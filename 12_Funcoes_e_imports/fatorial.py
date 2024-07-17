def fatorial_rec(n):
    # Com recursividade
    pass


def fatorial_non_rec(n):
    # Sem recursividade
    pass


# fatorial(5) = 5  * fatorial(4)
# fatorial(4) = 4  * fatorial(3)
# fatorial(3) = 3 * fatorial(2)
# fatorial(2) = 2 * fatorial(1)
# fatorial(1) = 1 * fatorial(0)
# fatorial(0) = 1

assert fatorial_rec(-1) is None
assert fatorial_rec(0) == 1
assert fatorial_rec(1) == 1
assert fatorial_rec(2) == 2
assert fatorial_rec(3) == 6
assert fatorial_rec(4) == 24
assert fatorial_rec(5) == 120

assert fatorial_non_rec(-1) is None
assert fatorial_non_rec(0) == 1
assert fatorial_non_rec(1) == 1
assert fatorial_non_rec(2) == 2
assert fatorial_non_rec(3) == 6
assert fatorial_non_rec(4) == 24
assert fatorial_non_rec(5) == 120

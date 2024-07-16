def fatorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * fatorial(n - 1)


print(fatorial(-1))

# fatorial(4) = 4  * fatorial(3)
# fatorial(3) = 3 * fatorial(2)
# fatorial(2) = 2 * fatorial(1)
# fatorial(1) = 1 * fatorial(0)
# fatorial(0) = 1

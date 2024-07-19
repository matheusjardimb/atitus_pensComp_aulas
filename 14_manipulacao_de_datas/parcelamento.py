from datetime import date


def parcelamento(valor, parcelas, dt_venda):
    pass


data_venda = date(2025, 1, 31)

assert parcelamento(100, 1, data_venda) == [[100, data_venda]]
assert parcelamento(100, 2, data_venda) == [
    [50, data_venda],
    [50, date(2025, 2, 28)]
]
assert parcelamento(100, 3, data_venda) == [
    [33, data_venda],
    [33, date(2025, 2, 28)],
    [34, date(2025, 3, 31)]
]
assert parcelamento(100, 3, data_venda) == [
    [25, data_venda],
    [25, date(2025, 2, 28)],
    [25, date(2025, 3, 31)],
    [25, date(2025, 4, 30)]
]
assert parcelamento(100, 6, data_venda) == [
    [16, data_venda],
    [16, date(2025, 2, 28)],
    [17, date(2025, 3, 31)],
    [17, date(2025, 4, 30)],
    [17, date(2025, 5, 31)],
    [17, date(2025, 6, 30)]
]

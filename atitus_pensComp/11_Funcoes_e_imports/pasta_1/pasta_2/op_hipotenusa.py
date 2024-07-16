from math import sqrt


def hipotenusa(cateto1, cateto2):
    soma_qdd = pow(cateto1, 2) + pow(cateto2, 2)
    return sqrt(soma_qdd)

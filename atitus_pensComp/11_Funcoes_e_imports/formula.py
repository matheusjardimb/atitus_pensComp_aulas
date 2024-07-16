from op_math.op_adicao import adicao
from op_math.op_subtracao import subtracao
from op_math.op_multip import multiplicacao
from op_math.op_divisao import divisao


def formula(a, b):
    # Sem usar os operadores matemácios (+, -, /, *)
    # return ((a + b) * (a - b)) / 2
    return divisao(multiplicacao(adicao(a, b), subtracao(a, b)), 2)


print(formula(10, 10))

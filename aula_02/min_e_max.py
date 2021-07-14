from math import inf

def calcular_min_max(lista_de_numeros):
    """
    O(n) Em tempo de execução
    O(1) Em memória

    :param lista_de_numeros:
    :return:
    """
    num_min = inf
    num_max = -inf
    for num in lista_de_numeros:
        if num > num_max:
            num_max = num
        if num < num_min:
            num_min = num
    return num_max, num_min


if __name__ == '__main__':
    print(calcular_min_max([2, 4, 2, 3, 6, 7]))



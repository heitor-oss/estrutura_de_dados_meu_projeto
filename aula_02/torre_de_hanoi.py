chamadas_hanoi_recursivo = 0

def _torre_de_hanoi_recursivo(numero_de_discos, origem, destino, auxiliar):
    """
    O(n**2) tempo de execução

    O(n) Memória

    :param numero_de_discos:
    :param origem:
    :param destino:
    :param auxiliar:
    :return:
    """

    global chamadas_hanoi_recursivo
    chamadas_hanoi_recursivo +=1
    if numero_de_discos == 1:
        print(f'{origem} -> {destino} : {numero_de_discos}')
        return
    _torre_de_hanoi_recursivo(numero_de_discos -1, origem, auxiliar, destino)
    print(f'{origem} -> {destino} : {numero_de_discos}')
    _torre_de_hanoi_recursivo(numero_de_discos -1, auxiliar, destino, origem)


def torre_de_hanoi(numero_de_discos: int):
    global chamadas_hanoi_recursivo
    chamadas_hanoi_recursivo = 0
    _torre_de_hanoi_recursivo(numero_de_discos, origem = 'A',
                              destino = 'B', auxiliar = 'C')
    pass

if __name__ == '__main__':
    for i in range(1, 5):
        print(f'#### hanoi para {i} discos')
        torre_de_hanoi(i)
        print(f'********{chamadas_hanoi_recursivo}')

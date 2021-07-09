from random import random
from math import inf
from time import time
def meu_max(iteravel):
    """
    Analise do algoritimo
    Tempo de execução O(n)
    Em memória O(1)

    :param iteravel:
    :return:
    """
    num_max = -inf
    for num in iteravel:
        if num > num_max:
            num_max = num
    return num_max

if __name__ == '__main__':
    print(meu_max([1, 10, 15 ,7]))
    inicio = 10
    for n in range(inicio, inicio * 20, inicio):
        start = time()
        meu_max(range(n))
        end = time()
        runtime = end - start
        print('*' * int(runtime + 1), runtime )




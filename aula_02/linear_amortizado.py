from itertools import cycle
from time import process_time, process_time_ns, perf_counter_ns

lista_de_numeros = list(range(10))
print(id(lista_de_numeros))
print(id(lista_de_numeros[0]))
print(id(lista_de_numeros[1]))
print(id(lista_de_numeros[2]))
lista_de_numeros.append(10)
print(id(lista_de_numeros))
lista_de_numeros.append('10')
print(id(lista_de_numeros))
maior_delta = 0
for i in cycle([11, 12]):
    id_final = id(lista_de_numeros)
    inicio = perf_counter_ns()
    lista_de_numeros.append(i)
    delta = perf_counter_ns() - inicio
    if delta > maior_delta:
        maior_delta = delta
    print(delta)

# sequencia mutavel

lista = list()

print(id(lista))
print(lista)
lista.append(1)
print(id(lista))
print(lista)

print('#####soma de lista')
lista = lista + [2, 4]
print(id(lista))

print('#####extend de lista ')
lista.extend([-2])
print(id(lista))

print('#####Sorted')
print(lista)
print(id(lista))
print(sorted(lista))
print(lista)

print('#####Sort')
print(lista)
print(id(lista))
print(lista.sort())
print(lista)

# sequencias imutaveis
print('Tupla')
tupla = (1, 2, 3)
print(id(tupla))
tupla += (4, 7)
print(id(tupla))

print('soma de string')
a = 'Heitor'
print(id(a))
a += 'Morais'
print(id(a))

print('##### objeto imutavel mutante')
tupla = (lista)
print(tupla)


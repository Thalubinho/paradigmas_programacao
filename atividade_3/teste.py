import util

lista = [1,2,3]
print(lista)
lista[0], lista[1] = lista[1], lista[0]
print(lista)
lista.append(5)
lista.append(6)
print(lista)
lista.pop(1)
print(lista)

print(util.filtraPares(lista))
print(lista)
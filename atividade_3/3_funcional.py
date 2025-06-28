import util
# Implementação imperativa do quicksort_pares utilizando o primeiro elemento como pivô

def quickSort_pares(lista):
    if lista == []:
        return []
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo and util.even(x)]
        meio = [x for x in [pivo] if util.even(x)]
        maiores = [x for x in lista[1:] if x > pivo and util.even(x)]

        return quickSort_pares(menores) + meio + quickSort_pares(maiores)

def quickSort(lista):
    if lista == []:
        return []
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]

        return quickSort(menores) + [pivo] + quickSort(maiores)

lista1 = [9, 1, 8, 2, 5, 7, 3, 6, 4]
lista2 = [3, 2, 7, 10, 23, 8, 1, 77, 8]

print("Implementação do quickSort recursivo funcional em python")
lista = lista1
print(quickSort(lista))

print("Implementação do quickSort recursivo funcional(apenas pares) em python")
lista = lista1
print(quickSort_pares(lista))



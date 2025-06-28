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

        return  quickSort_pares(maiores) + meio + quickSort_pares(menores)

def quickSort(lista):
    if lista == []:
        return []
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]

        return quickSort(menores) + [pivo] + quickSort(maiores)

lista1 = [9, 1, 8, 2, 5, 7, 3, 6, 4]

print("Implementação do quickSort recursivo funcional em python")
lista = lista1
print(quickSort(lista))

print("Implementação do quickSort recursivo funcional(apenas pares) em python")
lista = lista1
print(quickSort_pares(lista))



import util
# Implementação imperativa do quicksort utilizando o primeiro elemento como pivô
def quickSort(lista, pri, ult):
    if pri < ult:
        pivo = particao(lista, pri, ult)
        quickSort(lista, pri, pivo - 1)
        quickSort(lista, pivo + 1, ult)

def particao(lista, pri, ult):
    pivo = lista[pri]
    i = pri
    for j in range(pri + 1, ult + 1):
        if lista[j] <= pivo:
            i = i + 1
            util.troca(lista, i, j)

    util.troca(lista, pri, i)
    
    return i


lista1 = [9, 1, 8, 2, 5, 7, 3, 6, 4]
lista2 = [3, 2, 7, 10, 23, 8, 1, 77, 8]

print("Implementação do quickSort recursivo imperativo em python")
lista = lista1
quickSort(lista, 0, len(lista) - 1)
print(lista)


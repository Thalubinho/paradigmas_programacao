def even(x):
    return x % 2 == 0

def filtraPares(lista):
    lista = [x for x in lista if even(x)]

def contador():
    count = 0
    def incrementa():
        nonlocal count
        count += 1
        return count
    return incrementa

def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

# meuContador = contador()
# print(meuContador())
# print(meuContador())
# print(meuContador())
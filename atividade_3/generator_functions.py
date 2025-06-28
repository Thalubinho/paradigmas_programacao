def generate_ints(N):
   for i in range(N):
       yield i

gen = generate_ints(3)

print("Iterador com desempacotamento de sequência")
a, b, c = generate_ints(3)
print(a,b,c)
print("------------------------")

print("Iterador gerado apenas para o for ")
for i in generate_ints(3):
    print(i)
print("-----------------------")

print("Iterador gen")
for i in gen:
    print(i)
print("-------------")

# Note que iterar sobre um iterador esgotado nada acontece 
# e StopIteration não é lançada
print("Iterador gen")
for i in gen: 
    print(i)

print("-------------")

print(next(gen))
# Ao tentar chamar o iterador novamente, como já esgotamos todo os seus valores, 
# a execeção StopIteration é lançada

# TODO: Estudar Programação Orientada a Objetos com Python
# TODO: Estudar Herança Múltipla em Lua, vai ser importante para a continuação do projeto de PP
# TODO: definir uma classe manualmente para conseguir os efeitos de geradores(um gerador simples)
# TODO: passagem em ordem, pos ordem e pre ordem em uma arvores utilizando geradores de forma iterativa e recursiva
# TODO: testar os exemplos de geradores na biblioteca padrão do python lib/test/test_generators.py 
# existem muitas soluções interessante nesse teste: N-Queens,  Passeio do Cavalo)

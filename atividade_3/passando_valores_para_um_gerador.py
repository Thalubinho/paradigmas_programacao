def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # Se algum valor é recebido, o contador muda
        if val is not None:
            i = val
        else:
            i += 1

it = counter(10)
print(next(it))

print(next(it))

print(it.send(8))
# it.throw(value)
# it.close()

print(next(it))

print(next(it))
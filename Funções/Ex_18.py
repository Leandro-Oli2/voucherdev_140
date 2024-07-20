import random
lista = [12, 14, 17, 18, 22, 16, 29, 33, 72, 44, 23, 9, 1, 99, 17]
def somapar(tot, num):
    if num % 2 == 0:
        tot += num
    return tot
def sorteio(rdm):
    tot = 0
    for i in range(5):
        x = random.choice(rdm)
        print(x)
        tot = somapar(tot, x)
    return tot
s = sorteio(lista)
print(f"Soma dos Pares: {s}")

def maior(a, b, c):
    if a > b and a > c:
        print(f"O {a} eh o maior")
    elif b > a and b > c:
        print(f"O {b} eh o maior")
    else:
        print(f"O {c} eh o maior")

e = int(input("Informe um numero: "))
w = int(input("Informe outro numero: "))
q = int(input("Informe mais um numero: "))
maior(e, w, q)
def calculo(n1, n2, n3, letra):
    if letra == "A" or letra ==  "a":
        media = (n1+n2+n3)/3
        print(f"A media aritmetica eh {media}")
    elif letra == "P" or letra == "p":
        media = (n1*5 + n2*3 + n3*2)/n1+n2+n3
        print(f"A media Ponderada eh {media}")
    else:
        print("Letra Invalida!!")

n1 = float(input("Informe a nota1: "))
n2 = float(input("Informe a nota2: "))
n3 = float(input("Informe a nota3: "))
letra = input("Digite a letra(A ou P): ")
calculo(n1,n2,n3,letra)
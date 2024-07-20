num = int(input("Digite um numero: "))
def triangulo(n):
    for i in range(n):
        esp = ' ' * (n - i - 1)
        ast = '*' * (2 * i + 1)
        print(esp + ast)
triangulo(num)

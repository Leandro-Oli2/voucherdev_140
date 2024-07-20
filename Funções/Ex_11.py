def calculadora(a, b, operador):
    if operador == '+':
        result = a + b
        return result
    elif operador == '-':
        result = a - b
        return result
    elif operador == '/':
        result = a / b
        return result
    elif operador == '*':
        result = a*b
        return result
x = calculadora(5, 7, '+')
print(f"O resultado eh: {x}")

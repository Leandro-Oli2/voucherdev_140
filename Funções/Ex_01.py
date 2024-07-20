def pot(a, b):
    result = 0
    for i in range(1, b+1):
        result = a**i
        print(f"{a}**{i} = {result}")
pot(2,3)
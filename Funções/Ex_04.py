def convert(hora, min, seg):
    aux = hora*60
    aux1 = min*60
    tot = aux+aux1+seg
    print(f"A hora {hora}:{min}:{seg} em segundos eh: {tot}")
convert(16, 42, 32)
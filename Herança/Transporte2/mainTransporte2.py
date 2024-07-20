from Transporte import *
transporte_terrestre = Automovel(capacidade_passageiros=5, velocidade_maxima=180, tipo_terreno="Asfalto", tipo_combustivel="Gasolina")
print(transporte_terrestre)
transporte_terrestre.mover()
print()

    
aviao_mono = AviaoMonomotor(capacidade_passageiros=2, velocidade_maxima=300, envergadura=15, tipo_motor="Pistão")
print(aviao_mono)
aviao_mono.mover()
print()

aviao_comercial = AviaoComercial(capacidade_passageiros=200, velocidade_maxima=900, envergadura=45, numero_assentos=180)
print(aviao_comercial)
aviao_comercial.mover()
print()

    
lancha = Lancha(capacidade_passageiros=8, velocidade_maxima=60, tipo_propulsao="Motor de Popa", comprimento=8)
print(lancha)
lancha.mover()
print()

navio = Navio(capacidade_passageiros=200, velocidade_maxima=40, tipo_propulsao="Diesel", carga_maxima=5000)
print(navio)
navio.mover()
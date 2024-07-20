from Transporte import *
transporte_terrestre = Terrestre(capacidade_passageiros=5, velocidade_maxima=120, tipo_terreno="Asfalto")
print(transporte_terrestre)
transporte_terrestre.mover()
    
automovel = Automovel(capacidade_passageiros=4, velocidade_maxima=180, tipo_terreno="Terra", tipo_combustivel="Gasolina")
print(automovel)
automovel.mover()
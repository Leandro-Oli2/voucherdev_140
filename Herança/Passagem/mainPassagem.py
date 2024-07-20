from PassagemAviao import PassagemAviao
from PassagemBus import PassagemBus

passagem_aviao = PassagemAviao(preco=500, assento='A23', portaoD='B2', checkin='Online')
passagem_aviao.decolar()
print(f"Preço da passagem de avião: R${passagem_aviao.preco}")

passagem_onibus = PassagemBus(preco=100, assento='12B', placa='ABC1234', leito=True)
passagem_onibus.abastecer() 
print(f"Assento da passagem de ônibus: {passagem_onibus.assento}")
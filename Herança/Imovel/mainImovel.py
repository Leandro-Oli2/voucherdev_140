from Imovel import *

casa1 = Casa(inscricaoM="123456", valor_aluguel=1500.00, iptu=1200.00, quartos=3, piscina=True, area=200)
print(f"Parcela mensal do IPTU da Casa: R${casa1.obter_parcela_IPTU()}")
    
condominio1 = Condominio(inscricaoM="654321", valor_aluguel=2000.00, iptu=1800.00, elevador=True, area_de_lazer=True)
print(f"Parcela mensal do IPTU do Condomínio: R${condominio1.obter_parcela_IPTU()}")
    
apartamento1 = Apartamento(inscricaoM="987654", valor_aluguel=1800.00, iptu=1500.00, elevador=True, quartos=2)
print(f"Parcela mensal do IPTU do Apartamento: R${apartamento1.obter_parcela_IPTU()}")
    
terreno1 = Terreno(inscricaoM="456789", valor_aluguel=1000.00, iptu=1000.00, area=500)
print(f"Parcela mensal do IPTU do Terreno: R${terreno1.obter_parcela_IPTU()}")
    
chacara1 = Chacara(inscricaoM="789012", valor_aluguel=2500.00, iptu=2000.00, area=1000, churrasqueira=True)
print(f"Parcela mensal do IPTU da Chácara: R${chacara1.obter_parcela_IPTU()}")
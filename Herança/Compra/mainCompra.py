from Compra import *
compra_avista = Avista(numero=1, produto="Notebook", valor=2500.00, desconto=50.00)
compra_avista.calcular_valor_total()
print(compra_avista)
print(f"Preço com desconto: R${compra_avista.preco_com_desconto():.2f}")
    
compra_parcelada = Parcelada(numero=2, produto="Smartphone", valor=1500.00, numP=10)
compra_parcelada.calcular_valor_total()
print(compra_parcelada)
print(f"Valor de cada parcela: R${compra_parcelada.valor_parcela():.2f}")

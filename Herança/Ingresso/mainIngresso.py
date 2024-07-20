from Ingresso import Ingresso
from IngressoVIP import IngressoVIP

ingresso = Ingresso(230.67, "4c")
ingresso.alterar_preco(150.88)
ingresso.mostrar_setor()

ingressovip = IngressoVIP(True, True, True, True)
ingressovip.pegar_Bebida()
ingressovip.acessar_camarote()
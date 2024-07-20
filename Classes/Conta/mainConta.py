from Conta import Conta

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
saldo = float(input("Informe o saldo da conta: "))
while saldo < 0:
    saldo = float(input("Saldo negativo!, Informe novamente: "))

conta1 = Conta("Leandro","109.493.871-85", 67992253681, saldo)
dep = float(input("Informe o valor a depositar: "))
conta1.depositar(dep)
sac = float(input("Informe o valor a sacar: "))
conta1.sacar(sac)
conta1.imprimiSaldo()
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")



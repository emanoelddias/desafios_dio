menu = """

[d] Depositar 
[s] Sacar 
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado :"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}\n"
        else:
            print("Valor informado é negativo, por favor informe um valor valido")        

    elif opcao == "s":
        valor = float(input("Informe o valor a ser Sacado :"))

        if valor > saldo:
            print("Saldo insuficiente")
        
        elif valor > limite:
            print("Limite por operação excedido !! ")
        
        elif numero_saques > LIMITE_SAQUES:
            print("Limite de saques diarios excedido !! ")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Valor informado invalido")
    
    elif opcao == "e":
        print("Extrato")
        print("\n=======================EXTRATO=======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=====================================================")

    
    elif opcao == "q":
        break

    else:
        print("Operação inválida !")
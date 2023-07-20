menu = """

============== Banco ==============

Operações:
- D: depósito em conta
- S: saque de dinheiro
- E: extrato
- Q: sair da aplicação

"""

LIMITE_SAQUES = 3
LIMITE = 500

saldo = 0
saques_realizados = 0
extrato = ""

while True:
    cmd = input(menu).upper()
    
    match cmd:
        case 'D':
            deposito = float(input("Digite a quantidade a ser depositada: "))

            if deposito > 0:
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"

            else:
                print("O valor informado é inválido! Tente novamente!")
        case 'S':
            saque = float(input("Informe o valor do saque: "))

            if saque > saldo:
                print("O valor do saque excede o saldo da conta.")
            
            elif saques_realizados >= LIMITE_SAQUES:
                print("A quantidade máximas de saques já foi atingida (MAX.: 3 saques).")
            
            elif saque > LIMITE:
                print(f"O valor do saque ultrapassou o limite de saque: R${LIMITE},00.")
            
            elif saque > 0:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                saques_realizados += 1
            
            else:
                print("O valor informado é inválido! Tente novamente!")
        case 'E':
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
        case 'Q':
            print("Encerrando aplicação...")
            break
        case _:
            print("Operação Inválida! Tente outro comando!")
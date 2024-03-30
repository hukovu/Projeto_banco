# fluxo do caixa/dia

fluxo_caixa = []

print("----------")
print("@ Fluxo de Caixa por Dia: ")
print("----------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro número para encerrar #\n")


def adicionar_transacao():
    nome = input("Nome: ")
    valor = float(input("Valor (R$): "))
    fluxo_caixa.append({"nome": nome, "valor": valor})


while True:
    opcao = int(input("Opção: "))  

    if opcao == 1 or opcao == 2:  
        adicionar_transacao()
    else:
        break

# Mostrando o resultado
total = 0
for fc in fluxo_caixa:
    print("Nome:", fc['nome'], ", Valor: R$", fc['valor'])
    total += fc['valor'] 

print("Saldo atual: R$", total)
def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    for transacao in transacoes:

        tipo = "Depósito" if transacao > 0 else "Saque"
        print(tipo)
        transacao = float(transacao)
        saldo += transacao

        print(f"Transação: R$ {transacao}")
        print(saldo)
    
    return (f'Saldo R${saldo:.2f}')

entrada_usuario = input("[100, -50, 200]")

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")


transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:

resultado = calcular_saldo(transacoes)

print(resultado)

''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    for valor in transacoes:
        
        # TODO: Adicione o valor da transação ao saldo
        saldo += float(valor)

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    saldo_final = str(f"Saldo: R$ {saldo:.2f}")
    
    return saldo_final

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)
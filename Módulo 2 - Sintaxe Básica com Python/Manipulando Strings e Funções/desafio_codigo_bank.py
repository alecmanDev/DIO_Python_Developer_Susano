'''  CRIAR UM SISTEMA BANCÁRIO COM AS OPERAÇÕES: SACAR, DEPOSITAR E VISUALIZAR EXTRATO  '''

# Operações de depósito #
'''
    Deve ser possível depositar valores positivos para minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todo os depósitos devem ser armazenados em uma variável e exibidos em uma operação de extrato.
'''

# Operação de saque #
'''
    O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
'''

# Operação de vizualizar extrato #
'''
    Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
    Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
    1500.45 = R$ 1500,45
'''

import locale

# Menu
menu = '''
Seja bem-vindo ao NiantBank

Serviços:

[1] Depositar

[2] Saque

[3] Extrato

[4] Sair
'''

# Variáveis Globais
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

# Funções: Formatar moeda
def formatar_moeda(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, symbol=True, grouping=True)

while True:
    opcao = int(input(menu))
    
    # OPERAÇÃO DE DEPÓSITO
    if opcao == 1:
        print("OPÇÃO DE DEPÓSITO SELECIONADA: \n")

        saldo = float(input("Informe o valor que deseja depositar: "))
        if saldo >= 0:
            print(f"\nValor inserido com sucesso: {formatar_moeda(saldo)}\n")
        else:
            print("\nValor não reconhecido :(\n")

        extrato += f"Saldo: {saldo}\n" # Adcionando procedimento ao extrato

    # OPERAÇÃO DE SAQUE
    elif opcao == 2:
        print("OPÇÃO DE SAQUE SELECIONADA: \n")

        print(f"Limite de Saques: 3 \nVocê tem {LIMITE_SAQUE - numero_saque} saques disponíveis")
        valor_saq = float(input("Informe o valor que deseja sacar: "))
        
        if numero_saque <= 2:
            if valor_saq <= 500:
                if valor_saq <= saldo:
                    saldo -= valor_saq # Diferença do saldo
                    print(f"\nValor sacado: {formatar_moeda(valor_saq)}\nValor disponível: {formatar_moeda(saldo)}\n")

                    numero_saque += 1 # Adicionando número de saques utilizados

                    extrato += f"Saque: {valor_saq}\n" # Adcionando procedimento ao extrato
                else:
                    print(f"\nVocê não tem saldo disponível com o valor informado\n\nValor disponível: {formatar_moeda(saldo)}\n")
            else:
                print("Limite de R$ 500,00 por saque;")
        else:
            print("\nLimite de saques excedidos :(\n")
    else:
        print("Opção inválida")
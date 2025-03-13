'''  OTIMIZAÇÃO DO SISTEMA BANCÁRIO COM FUNÇÕES  '''
'''
Precisamos deixar nosso código mais modularizado para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)
'''
'''
# Função saque

A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato


# Função depósito

A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.


# Função extrato

A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.


# Novas funções: Criar usuário (cliente)

O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, numero - bairro - cidade/sigla estado. deve ser armazenado somente os números do CPF. Não podemos cadstrar 2 usuários com o mesmo CPF


# Novas funções: Criar conta corrente

O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

Dica:
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista

'''


import locale

# Menu
menu = '''
Seja bem-vindo ao NiantBank

Serviços:

[1] Criar usuário

[2] Criar conta corrente

[3] Depositar

[4] Saque

[5] Extrato

[6] Sair
'''

# Contantes
AGENCIA = "0001"
LIMITE_SAQUE = 2

# Variáveis Globais
usuarios = []
contas = []

# Funções: Formatar moeda
def formatar_moeda(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, symbol=True, grouping=True)

# Funções: Criar uma conta
def criar_usuario():
    nome = input("Insira seu nome completo: ")
    data_nascimento = input("Insira sua data de nascimento (DD/MM/AAAA): ")
    cpf = input("CPF (Apenas números): ").strip().replace(".", "").replace("-", "")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade_uf = input("Cidade/UF (Exmeplo: Marituba/PA): ")

    endereco = {
        "logradouro": logradouro,
        "numero": numero,
        "bairro": bairro,
        "cidade_uf": cidade_uf
    }

    if any(usuario["cpf"] == cpf for usuario in usuarios): # Verificando se o CPF já está cadastrado
        print("Usuário já cadastrado!") # Mensagem de erro
        return # Retornando para o menu
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) # Adcionaando ao dicionário de usuários
    print("\nUsuário cadastrado com sucesso!\n")

def criar_conta():
    cpf = input("CPF do usuário: ").strip().replace(".", "").replace("-","") # Usuário informa o CPF
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None) # Verifica se o CPF informado se localiza no dicionário 'usuário'
    if not usuario: # Caso não encontre, dá erro!
        print("Usuário não encontrado!")
        return
    
    conta = len(contas) + 1 # Conta é sequencial, seguindo sempre com mais 1

    contas.append({"agencia": AGENCIA, "conta": conta, "usuario": usuario}) # Adciona as informações ao dicionário 'CONTAS'
    print(f"\nConta criada com sucesso!\nAGÊNCIA: {AGENCIA} | CONTA: {conta}\n")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: {formatar_moeda(valor)} | Saldo atual: {formatar_moeda(saldo)}\n"
        print(f"\nDepósito realizado com sucesso: {formatar_moeda(valor)}\n")

    else:
        print("Valor informado inválido")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques > limite_saques:
        print("Limite de saques atingidos hoje!")
    elif valor > saldo:
        print(f"Valor informado excede o saldo atual de {formatar_moeda(saldo)}")
    elif valor > limite:
        print(f"Valor informado excede o limite de {formatar_moeda(limite)}")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: {formatar_moeda(valor)} | Saldo atual: {formatar_moeda(saldo)}\n"
        numero_saques += 1
        print(f"\nSaque realizado com sucesso: {formatar_moeda(valor)}\n")
    else:
        print("Valor informado inválido")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ===============\n")
    print(extrato if extrato else "Não foram realizadas movimentações nesta conta!")
    print(f"\n\nSaldo atual da conta: {formatar_moeda(saldo)}\n\n")
    print("=========================================\n")

# Programa principal
saldo = 0
extrato = ""
numero_saques = 0

while True:
    opcao = int(input(menu))
    
    # OPERAÇÃO DE CRIAÇÃO DE USUÁRIO
    if opcao == 1:
        print("OPÇÃO DE CRIAÇÃO DE USUÁRIO SELECIONADA: \n")
        criar_usuario()

    # OPERAÇÃO DE CRIAÇÃO DE CONTA CORRENTE
    elif opcao == 2:
        print("OPÇÃO DE CRIAÇÃO DE CONTA COORENTE SELECIONADA: \n")
        criar_conta()

    # OPERAÇÃO DE DEPOSITAR
    elif opcao == 3:
        print("OPÇÃO DE DEPÓSITO SELECIONADA: \n")
        valor = float(input("Informe o valor que deseja depositar: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    # OPERAÇÃO DE SACAR
    elif opcao == 4:
        print("OPÇÃO DE SAQUE SELECIONADA: \n")
        valor = float(input("Informe o valor que deseja sacar: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=500, numero_saques=numero_saques, limite_saques=LIMITE_SAQUE)

    # OPERAÇÃO DE EXIBIR EXTRATO
    elif opcao == 5:
        print("OPÇÃO DE EXTRATO SELECIONADA: \n")
        exibir_extrato(saldo, extrato=extrato)

    # OPERAÇÃO DE SAÍDA DO SISTEMA
    elif opcao == 6:
        print("OBRIGADO POR UTILIZAR O SISTEMA NIANTBANK")
        break
    
    else:
        print("Opção inválida")
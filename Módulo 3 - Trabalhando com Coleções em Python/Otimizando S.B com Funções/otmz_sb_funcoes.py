'''  OTIMZAÇÃO DO SISTEMA BANCÁRIO COM FUNÇÕES  '''
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

[1] Depositar

[2] Saque

[3] Extrato

[4] Sair
'''

# Contantes
AGENCIA = "0001"
LIMITE_SAQUE = 3

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
    data_nascimento = input("Insira sua data de nascimento (DD/MM/AAAA)")
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
    print("Usuário cadastrado com sucesso!")

def criar_conta():
    cpf = input("CPF do usuário: ").strip().replace(".", "").replace("-","") # Usuário informa o CPF
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None) # Verifica se o CPF informado se localiza no dicionário 'usuário'
    if not usuario: # Caso não encontre, dá erro!
        print("Usuário não encontrado!")
        return
    
    conta = len(contas) + 1 # Conta é sequencial, seguindo sempre com mais 1

    contas.append({"agencia": AGENCIA, "conta": conta, "usuario": usuario}) # Adciona as informações ao dicionário 'CONTAS'
    print(f"Conta criada com sucesso!\nAGÊNCIA: {AGENCIA} | CONTA: {conta}")

while True:
    opcao = int(input(menu))
    
    # OPERAÇÃO DE DEPÓSITO
    if opcao == 1:
        print("OPÇÃO DE DEPÓSITO SELECIONADA: \n")

        deposito = float(input("Informe o valor que deseja depositar: "))
        if deposito >= 0:
            print(f"\nValor inserido com sucesso: {formatar_moeda(deposito)}\n")

        else:
            print("\nValor não reconhecido :(\n")
        
        saldo = saldo + deposito
        extrato += f"Aplicação: {formatar_moeda(deposito)}\nSaldo na conta: {formatar_moeda(saldo)}\n\n" # Adcionando procedimento ao extrato

    # OPERAÇÃO DE SAQUE
    elif opcao == 2:
        print("OPÇÃO DE SAQUE SELECIONADA: \n")

        print(f"Limite de Saques: 3 \nVocê tem {LIMITE_SAQUE - numero_saque} saques disponíveis")
        valor_saq = float(input("Informe o valor que deseja sacar: "))
        
        if numero_saque <= 2:
            if valor_saq <= 500:
                if valor_saq <= saldo and valor_saq != 0:
                    saldo -= valor_saq # Diferença do saldo
                    print(f"\nValor sacado: {formatar_moeda(valor_saq)}\nValor disponível: {formatar_moeda(saldo)}\n")

                    numero_saque += 1 # Adicionando número de saques utilizados

                    extrato += f"Saque: {formatar_moeda(valor_saq)}\nSaldo na conta: {formatar_moeda(saldo)}\n\n" # Adcionando procedimento ao extrato
                else:
                    print(f"\nVocê não tem saldo disponível com o valor informado\n\nValor disponível: {formatar_moeda(saldo)}\n")
            else:
                print("Limite de R$ 500,00 por saque;")
        else:
            print("\nLimite de saques excedidos :(\n")

    # OPERAÇÃO DE EXTRATO
    elif opcao == 3:
        print("OPÇÃO DE EXTRATO SELECIONADA: \n")
        print("================ EXTRATO ===============\n")
        print(extrato)
        print("=========================================")

    # OPERAÇÃO DE SAÍDA DO SISTEMA
    elif opcao == 4:
        print("OBRIGADO POR UTILIZAR O SISTEMA NIANTBANK")
        break
    
    else:
        print("Opção inválida")
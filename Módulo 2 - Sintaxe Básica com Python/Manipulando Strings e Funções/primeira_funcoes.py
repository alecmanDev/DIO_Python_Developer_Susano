# É um bloco de código identificado por um nome e pode receber uma lista de parâmetros

def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Antônio"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Alessandro")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

# Retornando valores
# Para retornar um valor, utilizamos a palavra 'return'

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10, 20, 34]) # 64
retorna_antecessor_sucessor(10) # (9, 11)

# Argumentos nomeados
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Saída 1
salvar_carro("Palio", "Fiat", 1999, "ABC-1234")

# Saída 2
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# Saída 3
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
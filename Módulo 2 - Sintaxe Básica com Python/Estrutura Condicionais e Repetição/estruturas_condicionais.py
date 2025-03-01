# Permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas

# if
saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print ("Saldo insuficiente!")

# if e else
saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print ("Saldo insuficiente!")

# if/elif/else
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ...
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida")
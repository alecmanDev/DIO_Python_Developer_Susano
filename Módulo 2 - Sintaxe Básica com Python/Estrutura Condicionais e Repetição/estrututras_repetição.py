# Estruturas utilizadas para repetir um trecho de código um determinado número de vezes

a = int(input("Informe um número inteiro: "))

a += 1
print(a)

a += 1
print(a)

# ==================================

# Comando for usando um iterável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adciona uma quebra de linha

# Função range
list(range(4))
# >>> [0, 1, 2, 3]

range(0, 10)
print(list(range(0, 10)))

# Utilizando range com for
for numero in range(0, 11):
    print(numero, end=" ")

# Exemplo: Exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

# Commando while
# É usado para repetir um bloco de código várias vezes

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n: "))

    if opcao == 1:
        print("Sacado...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar o sistema bancário, até logo!")

# while com break
for numero in range(100):

    if numero == 12:
        print(numero, end=" ")
        break
    
    elif numero == 25:
        print(numero, end=" ")
        continue
        
    elif numero % 2 == 0:
        print(numero, end=" ")
        continue
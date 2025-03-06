# Listas
''' Listas em python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por vírgula dentro de colchetes'''

frutas = ["laranja", "maça", "uva"] # Padrão de listas

frutas = [] # Pode ser vazia

letras = list("python") # Vai separar a stuing 'python' letra por letra -> ["p", "y", "o", "t", "h", "o", "n"]

numeros = list(range(10)) # Confere de 1 a 9

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True] # Mistura diversos tipos de dados

# Acesso direto #
frutas = ["laranja", "maça", "uva"]

frutas[0] # laranja
frutas[2] # uva

# Índices negativos
frutas[-1] # uva
frutas[-2] # maça

# Listas aninhadas
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"],
]

# Lê-se -> Linha[] e Coluna[] 
matriz[0] # [1, "a", 2] Linha 1
matriz[0][0] # 1 Linha 1 Coluna 1 (1,1)
matriz[0][-1] # 2 Linha 1 Coluna 3 (1,3)
matriz[-1][-1] # "c" # Linha 3 Coluna 3 (3,3)

# Fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"] 

# Iterar listas utilizando o 'for'
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# Função enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Compreensão de listas: filtro versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares, "Exemplo 1")

# Compreensão de listas: filtro versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares, "Exemplo 2")

# Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado, "Exemplo 1")

# Modificando valores versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(numero, "Exemplo 2")

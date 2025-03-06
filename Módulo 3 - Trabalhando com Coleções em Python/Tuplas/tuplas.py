''' Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que a Tupla é imutável (os valores podem ser modificados), a lista é mutável (os valores podem mudar com o tempo) '''

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)


# Acesso direto
frutas = ("laranja", "pera", "uva",)

frutas[0] # laranja
frutas[1] # pera
frutas[-1] # uva

# Tupla aninhada
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

# Lê-se -> Linha[] e Coluna[] 
matriz[0] # [1, "a", 2] Linha 1
matriz[0][0] # 1 Linha 1 Coluna 1 (1,1)
matriz[0][-1] # 2 Linha 1 Coluna 3 (1,3)
matriz[-1][-1] # "c" # Linha 3 Coluna 3 (3,3)


# ().count -> Confere a quantidade de elementos x tem dentro da tupla4

# ().index -> Verifica a posição

# len() -> Quantidade de elementos da tupla
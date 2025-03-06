''' Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados  de um objeto iterável'''

# Usando parênteses
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"} -> O set não deixa ordenado

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"} -> O set não deixa ordenado

carros = set(("palio", "celta", "honda fit", "palio"))
print(carros)

# Acessando os dados, deve ser convertido para lista
numeros = {1, 2, 3, 4}

numeros = list(numeros)
print(numeros[0])


# Iterar conjuntos
carros = {"palio", "celta", "honda fit", "palio"}

for carro in carros:
    print(carro)

# Metódos da classe set

# {}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}


# {}.intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3}


# {}.difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}


# {}.symmetric_difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}


# {}.issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False


# {}.issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True


# {}.isdisjoint

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False


# {}.add

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}


# {}.clear

sorteio = {1, 23}

sorteio.clear() # {}

# {}.copy -> Parecido com a da lista

# {}.discard

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)

numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}

# {}.pop -> Parecido com o das listas e tupla

# {}.remove -> Parecido com o das listas e tupla

# len

# in
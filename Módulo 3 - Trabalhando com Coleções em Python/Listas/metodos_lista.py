# [].append()

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Pyhton", [40, 30, 20]]


# [].clear()

lista = [1, "Pyhton", [40, 30, 20]]

print(lista, "Usando Clear")
lista.clear()
print(lista) # []


# [].copy()

lista = [1, "Pyhton", [40, 30, 20]]

l2 = lista.copy()

print(id(l2), id(lista))

l2[0] = "alec"

print(lista, " e ", l2)


# [].extend()
linguagens = ["js", "python", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)


# [].index()
linguagens = ["java", "python", "c", "java", "csharp"]

print(linguagens.index("java"))
print(linguagens.index("python"))


# [].pop()
linguagens = ["js", "python", "c", "java", "csharp"]

linguagens.pop() # csharp
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # js


# [].remove()
linguagens = ["java", "python", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens) # ["java", "python", "java", "csharp"]


# [].reverse()
linguagens =["java", "python", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens) 


# [].sort()
linguagens = ["java", "python", "c", "java", "csharp"]
linguagens.sort() # Reorganiza a lista em ordem alfabética
print(linguagens)

linguagens = ["java", "python", "c", "java", "csharp"]
linguagens.sort(reverse=True) # Reorgazniza a lista em oredem alfabética reversa
print(linguagens)

linguagens = ["java", "python", "c", "java", "csharp"]
linguagens.sort(key=lambda x:len(x)) # Reordena pela quantidade de caracteres em cada item

linguagens = ["java", "python", "c", "java", "csharp"]
linguagens.sort(key=lambda x:len(x), reverse=True) # Reordena pela quantidade de caracteres em cada item, reversamente

# len
linguagens = ["java", "python", "c", "java", "csharp"]
len(linguagens) # 5


# sorted, parecido com o metódo sort, a diferença é que o sorted é uma função
linguagens = ["java", "python", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # Reordena pela quantidade de caracteres em cada item
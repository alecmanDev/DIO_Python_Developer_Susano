# Old style %

nome = "Alessandro"
idade = 28
profissao = "Programador"
linguagem =  "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# Método format

nome = "Alessandro"
idade = 28
profissao = "Programador"
linguagem =  "Python"

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(nome, idade, profissao, linguagem))

# f-string

nome = "Alessandro"
idade = 28
profissao = "Programador"
linguagem =  "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Formatar strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")
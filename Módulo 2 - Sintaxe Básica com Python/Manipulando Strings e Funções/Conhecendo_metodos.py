# Metódos úteis para manipular objetos do tipo string

# Maiúscula, minúscula e título
curso = "pYtHon"

print(curso.upper())
# >>> PYTHON

print(curso.lower())
# >>> python

print(curso.title())
# >>> Python

# Eliminando espaços em branco
curso1 = "    JavaScript  "

print(curso1.strip())
# >>> "JavaScript"

print(curso1.lstrip())
# >>> "JavaScript  "

print(curso.rstrip())
# >>> "    JavaScript"

# Junções e centralizações
curso = "Angular"

print(curso.center(10, "#"))
# >>> "##Angular##"

print(".".join(curso))
# >>> "A.n.g.u.l.a.r"


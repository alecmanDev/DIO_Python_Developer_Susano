# São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica, retorna true or false

# Operador E (and)
# Ambos os lados devem ser verdade para retorna TRUE

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite

# Operador OU (or)
# Pelo menos um for verdade, retorna TRUE

saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite

# Operador Negação (not)
# É o inverso da verdade

not 1000 > 1500

not "saque 1500;"

not ""

# Procedimento de saque de dinheiro
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)
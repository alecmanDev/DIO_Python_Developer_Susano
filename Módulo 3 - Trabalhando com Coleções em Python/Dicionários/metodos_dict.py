# {}.clear

# {}.copy

# {}.fromkeys

dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": "None"}

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

# {}.get
contatos ={
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}
}

#contatos["chave"] #KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {})


# {}.items -> Retorna os itens presentes na tupla

# {}.keys -> Retorna chaves do dicionário

# {}.pop -> Remove e retorna algum valor definido

# {}.popitem -> Remove os itens na sequência

# {}.setdefault
contatos ={
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}
}

#contatos.setdefault("nome", "Giovanna") # Guilherme
#print(contatos)

contatos.setdefault("idade", 28) #28
print(contatos) # {'nome': 'Guiilherme', 'telefone': '3333-1234', 'idade': 28}


# {}.update
contatos ={
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)


contatos.update({"giovana@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contatos) # {"guilherme@gmail.com": {"nome": "Gui"}, "giovana@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}}


# {}.values -> Ele retorna os valores das chaves, não as chaves

# in -> Verificar se uma chave X existe no dicionário, etc

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3434-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}
}

resultado = "guilherme@gmail.com" in contatos # True
print(resultado)

resultado = "giovanna@gmail.com" in contatos # True
print(resultado)

resultado = "meuid@gmail.com" in contatos # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"] # False
print(resultado)


# del

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3434-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

print(contatos) 
'''
{
    "guilherme@gmail.com": {"nome": "Guilherme"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3434-2121"},
}
'''


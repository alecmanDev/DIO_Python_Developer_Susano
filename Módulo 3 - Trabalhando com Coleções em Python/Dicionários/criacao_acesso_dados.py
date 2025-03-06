''' Em Python, um dicionário (dict) é uma estrutura de dados que armazena valores em pares chave: valor. Ele é útil para armazenar e acessar informações de maneira eficiente, semelhante a um "banco de dados" simples.

✅ Principais características:
✔ Armazena pares chave-valor.
✔ As chaves são únicas e imutáveis (strings, números ou tuplas).
✔ Os valores podem ser de qualquer tipo (listas, strings, números, outros dicionários, etc.).
✔ Acesso rápido aos valores através das chaves. '''

pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3333-1234" # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}


# Acesso dos dados

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"] # Guilherme
dados["idade"] # 28
dados["telefone"] # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = "19"


# Diciionários aninhados

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3434-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}
}

cont = contatos["giovanna@gmail.com"]["telefone"] # "3434-2121"
print(cont)


# Iterar dicionários

for chave in contatos:
    print(chave, contatos[chave]) # Faz ter o acesso aos valores do dicionário

for chave, valor in contatos.items():
    print(chave, valor) # Tem o mesmo resultado de forma mais simples
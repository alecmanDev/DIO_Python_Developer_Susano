# Construtores e Destrutores

'''
🛠️ 1. Construtor (__init__)
O construtor é um método especial chamado automaticamente quando um objeto é criado.
Ele é usado para inicializar os atributos da classe.

💥 2. Destrutor (__del__)
O destrutor (__del__) é chamado automaticamente quando um objeto é destruído, ou seja, quando ele não é mais necessário.
'''

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe")

    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Zag", "Branco e preto", False)
    print(c.nome)

c = Cachorro("Chappie", "amarelo")
c.falar()

print("hello")
print("hello")

del c

print("hello")
print("hello")
print("hello")
criar_cachorro()
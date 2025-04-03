class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Alec", 2005)
print(f"Nome: {pessoa.nome} \t Idade: {pessoa.idade}")
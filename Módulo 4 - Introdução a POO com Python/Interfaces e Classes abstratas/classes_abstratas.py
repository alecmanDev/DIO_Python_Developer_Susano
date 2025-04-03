from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    

    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligada")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligando!")

    @property
    def marca(self):
        return "LG"


class ControleArcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligando!")

    @property
    def marca(self):
        return "Philco"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArcondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

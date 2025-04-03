'''
🔥 O que é Polimorfismo em POO?
✅ Definição
Polimorfismo é um conceito da Programação Orientada a Objetos (POO) que permite que um mesmo método tenha diferentes comportamentos dependendo da classe que o implementa.

🔹 Em outras palavras: Objetos de diferentes classes podem ser tratados de forma uniforme, desde que implementem os mesmos métodos.
'''

print(len("python"))
print(len([10, 20, 30]))

'''
Polimorfismo com herança
'''

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(ob):
    ob.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)
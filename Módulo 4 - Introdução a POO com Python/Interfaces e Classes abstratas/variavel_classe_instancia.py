class Estudante:
    escola = "DIO" # Variavel de classe

    def __init__(self, nome, matricula):
        self.nome = nome # Variavel de Instância
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Alec", 2)

print(aluno_1)
print(aluno_2)

Estudante.escola = "Cectrum"
aluno_1.matricula = 3
aluno_2.matricula = 10

aluno_3 = Estudante("Chappie", 4)

mostrar_valores(aluno_1, aluno_2, aluno_3)
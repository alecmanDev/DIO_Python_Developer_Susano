# Recursos públicos e privados

# Modificadores de acesso
# Público: Pode ser acessado de fora da classe
# Privado: Só pode ser acessado pela classe

'''
🏷️ Níveis de Acesso no Python
Python não tem modificadores de acesso como private, protected e public explícitos (como Java ou C++), mas utiliza convenções:

Modificador	Exemplo	Acessível de fora da classe?
Uso típico
Público	self.atributo	✅ Sim	Pode ser acessado diretamente

Protegido (_)	self._atributo	⚠️ Sim (mas não recomendado)	Indica que é "privado", mas pode ser acessado se necessário

Privado (__)	self.__atributo	❌ Não (mas pode ser acessado com "name mangling")	

'''

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # Privado
        self.nro_agencia = nro_agencia # Público
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
    

conta = Conta("0001", 100)
conta.depositar(100)
# print(conta._saldo) -> Por ser privado, não devemos modificar fora da classe
print(conta)
print(conta.mostrar_saldo())
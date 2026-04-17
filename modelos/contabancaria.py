
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Titular: {self._titular}, Saldo: R${self._saldo:.2f}"
    
    def ativar_conta(self):
        self._ativo = True
        print(f"Conta de {self._titular} ativada.")

    @property 
    def saldo(self):
        return self._saldo
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def ativo(self):
        return "✔️" if self._ativo else "❌"  
    
class ClienteBanco:
    def __init__(self, nome, idade, cpf, email, saldo):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._email = email
        self._saldo = saldo

    def __str__(self):
        return f"Cliente: {self._nome}, Idade: {self._idade}, CPF: {self._cpf}, Email: {self._email}, Conta: {self._saldo:.2f}"
    
    @classmethod
    def criar_conta(cls, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        return conta



conta1 = ContaBancaria("Rodrigo", 1000.00)
conta2 = ContaBancaria("Clara", 500.00)
conta2.ativar_conta()

print(conta1)
print(conta2)
print(conta1._saldo)

cliente1 = ClienteBanco(conta1._titular, 30, "123.456.789-00", "rodrigo@email.com", 1000.00)
cliente2 = ClienteBanco(conta2._titular, 25, "987.654.321-00", "clara@email.com", 500.00)
cliente3 = ClienteBanco("João", 25, "987.654.321-00", "joao@email.com", 10.00)

print(cliente1)
print(cliente2)
print(cliente3)

conta_joao = ClienteBanco.criar_conta(cliente3._nome, cliente3._saldo)
print(conta_joao)


class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.profissao = profissao
        self.idade = idade

    def __str__(self):
        if self.profissao:
           return f"{self.nome} é {self.profissao} e tem {self.idade} anos"
        else: 
            return f"{self.nome} tem {self.idade} anos"
    
    def aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome}! Agora você tem {self.idade} anos.")

    def saudacao(self):
        if self.profissao:
           print(f"Olá, meu nome é {self.nome} e sou {self.profissao}.")
        else:
            print(f"Olá, meu nome é {self.nome}.")

# Criando instâncias da classe Pessoa
pessoa1 = Pessoa("Rodrigo", 30, 'Engenheiro')
pessoa2 = Pessoa("Maria", 25, 'Médica')
pessoa3 = Pessoa("João", 40)

# Imprimindo as informações das pessoas
print(pessoa1)
print(pessoa2)
print(pessoa3)

# Utilizando os métodos de aniversário e saudação
pessoa1.aniversario()
pessoa2.saudacao()
pessoa3.aniversario()
pessoa3.saudacao()
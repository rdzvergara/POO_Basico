

class Cliente:
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

cliente1 = Cliente("Rodrigo", 30, "123.456.789-00", "rodrigo@hotmail.com")
cliente2 = Cliente("Maria", 25, "987.654.321-00", "maria@gmail.com")
cliente3 = Cliente("João", 40, "111.222.333-44", "teste@outlook.com")
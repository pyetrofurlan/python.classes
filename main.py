class Cliente:
    def __init__(self, nome, ano_nascimento, sexo, saldo, endereco, ativo):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.sexo = sexo
        self.saldo = saldo
        self.endereco = endereco
        self.ativo = ativo
    
    def imprimir_dados(self):
        print("Nome:", self.nome)
        print("Ano de Nascimento:", self.ano_nascimento)
        print("Sexo:", self.sexo)
        print("Saldo:", self.saldo)
        print("Endereço:", self.endereco)
        print("Ativo:", self.ativo)
    
    def verificar_ativo(self):
        if self.ativo:
            print("O cliente está ativo.")
        else:
            print("O cliente está inativo.")
    
    def calcular_idade(self, ano_atual):
        idade = ano_atual - self.ano_nascimento
        print("Idade do Cliente:", idade)
    
    def verificar_saldo(self):
        if self.saldo >= 0:
            print("O saldo do cliente é positivo.")
        else:
            print("O saldo do cliente é negativo.")


cliente1 = Cliente("João", 2006, "Masculino", 1000, "Rua A, 123", True)
cliente2 = Cliente("Maria", 2006, "Feminino", -500, "Rua B, 456", True)
cliente3 = Cliente("Pedro", 2007, "Masculino", 2000, "Rua C, 789", False)


print("Dados do Cliente 1:")
cliente1.imprimir_dados()
print("\nDados do Cliente 2:")
cliente2.imprimir_dados()
print("\nDados do Cliente 3:")
cliente3.imprimir_dados()


print("\nStatus de Atividade dos Clientes:")
cliente1.verificar_ativo()
cliente2.verificar_ativo()
cliente3.verificar_ativo()


ano_atual = 2024
print("\nIdade dos Clientes:")
cliente1.calcular_idade(ano_atual)
cliente2.calcular_idade(ano_atual)
cliente3.calcular_idade(ano_atual)


print("\nStatus do Saldo dos Clientes:")
cliente1.verificar_saldo()
cliente2.verificar_saldo()
cliente3.verificar_saldo()

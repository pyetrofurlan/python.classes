class Cadastro:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.saldo = None
        self.statusCadastro = None
        self.endereco = None

    def inserir_nome(self, nome):
        if self.valida_nome(nome):
            self.nome = nome
            print("Nome cadastrado com sucesso")
        else:
            print("Erro ao cadastrar nome")

    def inserir_idade(self, idade):
        if self.valida_idade(idade):
            self.idade = idade
            print("Idade cadastrada com sucesso")
        else:
            print("Erro ao cadastrar idade")

    def inserir_saldo(self, saldo):
        if self.valida_saldo(saldo):
            self.saldo = saldo
            print("Saldo cadastrado com sucesso")
        else:
            print("Erro ao cadastrar saldo")

    def inserir_status_cadastro(self, statusCadastro):
        if self.valida_status_cadastro(statusCadastro):
            self.statusCadastro = statusCadastro
            print("Status de cadastro cadastrado com sucesso")
        else:
            print("Erro ao cadastrar status de cadastro")

    def inserir_endereco(self, endereco):
        if self.valida_endereco(endereco):
            self.endereco = endereco
            print("Endereço cadastrado com sucesso")
        else:
            print("Erro ao cadastrar endereço")

    def valida_nome(self, nome):
        if len(nome) > 0:
            return True
        else:
            return False

    def valida_idade(self, idade):
        if idade > 18:
            return True
        else:
            return False

    def valida_saldo(self, saldo):
        if saldo >= 0:
            return True
        else:
            return False

    def valida_status_cadastro(self, statusCadastro):
        if statusCadastro:
            return True
        else:
            return False

    def valida_endereco(self, endereco):
        if len(endereco) >= 3:
            return True
        else:
            return False

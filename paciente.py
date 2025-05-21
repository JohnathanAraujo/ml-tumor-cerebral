class Paciente:
    def __init__(self, nome, cpf, prioridade):
        self.nome = nome
        self.cpf = cpf
        self.prioridade = prioridade

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf}, Prioridade: {self.prioridade})"
    
    def salvarImagem(self, nome, cpf):
        self.cpf = cpf
        imagem = ("pathNome")
        if imagem == "path + nome" :
            return imagem

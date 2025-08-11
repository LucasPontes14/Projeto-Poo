class Funcionario():
    def __init__(self, nomeFuncionario, senha, id = None):
        self.nomeFuncionario = nomeFuncionario
        self.senha = senha
        self.id = id
        self.status = "ativo"
    
    def to_dict(self):
        return {
            "nomeFuncionario": self.nomeFuncionario,
            "senha": self.senha,
            "id": self.id,
            "status": self.status
        }
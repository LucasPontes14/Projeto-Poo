class Visitante():
    def __init__(self, nomeUsuario, senha, id = None, estaCadastrado = False):
        self.nomeUsuario = nomeUsuario
        self.senha = senha
        self.estaCadastrado = estaCadastrado
        self.id = id
        self.emprestimos = []

    def to_dict(self):
         return {
            "nomeUsuario": self.nomeUsuario, 
            "senha": self.senha,
            "estaCadastrado": self.estaCadastrado,
            "id": self.id,
            "emprestimos": [emprestimo.to_dict() for emprestimo in self.emprestimos] 
        }
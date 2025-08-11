class Autor:
    def __init__(self, nomeAutor, id, emailAutor, livrosAutor = None):
        self.nomeAutor = nomeAutor
        self.id = id
        self.emailAutor = emailAutor
        self.livrosAutor = livrosAutor if livrosAutor is not None else []

    def to_dict(self):
        return {
            "nomeAutor": self.nomeAutor, 
            "id": self.id,
            "emailAutor": self.emailAutor,
            "livrosAutor": self.livrosAutor
        }
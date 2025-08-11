class Exemplar:
    def __init__(self, livro_id, codigoExemplar, estaDisponivel = True, id= None):
        self.estaDisponivel = estaDisponivel
        self.livro_id = livro_id
        self.codigoExemplar = codigoExemplar
        self.id = id
    
    def to_dict(self):
        return {
            "livro_id": self.livro_id,
            "estaDisponivel": self.estaDisponivel,
            "codigoExemplar": self.codigoExemplar,
            "id": self.id
        }
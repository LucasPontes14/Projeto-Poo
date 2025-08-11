class Editora:
    def __init__(self, nomeEditora, id = None):
        self.nomeEditora = nomeEditora
        self.id = id

    def to_dict(self):
        return {
            "nomeEditora": self.nomeEditora,
            "id": self.id
        }
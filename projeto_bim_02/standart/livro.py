class Livro:
    def __init__(self, codigoLivro, nomeLivro, autorLivro, dataEdicao, formato, editoraLivro, exemplaresLivro = None,id = None):
        self.nomeLivro = nomeLivro
        self.autorLivro = autorLivro
        self.dataEdicao = dataEdicao
        self.editoraLivro = editoraLivro
        self.codigoLivro = codigoLivro
        self.id = id
        self.formato = formato
        self.exemplaresLivro = exemplaresLivro if exemplaresLivro is not None else []
    
    def to_dict(self):
        return {
            "nomeLivro": self.nomeLivro,
            "autorLivro": self.autorLivro,
            "dataEdicao": self.dataEdicao,
            "editoraLivro": self.editoraLivro,
            "codigoLivro": self.codigoLivro,
            "id": self.id,
            "formato": self.formato,
            "exemplaresLivro": self.exemplaresLivro
        }
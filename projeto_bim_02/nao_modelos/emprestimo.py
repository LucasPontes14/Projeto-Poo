class Emprestimo:
    def __init__(self, exemplar, usuario, dataEmprestimo, dataEntregaPrevista):
        self.usuario = usuario
        self.exemplar = exemplar
        self.dataEmprestimo = dataEmprestimo
        self.dataEntregaPrevista = dataEntregaPrevista
        self.dataEntregaRealizada = None
        self.multa = 0.0
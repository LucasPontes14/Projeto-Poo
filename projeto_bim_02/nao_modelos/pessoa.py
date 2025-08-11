from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nomeUsuario, senha):
        self.nomeUsuario = nomeUsuario
        self.senha = senha

    @abstractmethod
    def cadastrar(ABC):
        pass

    @abstractmethod
    def entrar(ABC):
        pass

    @abstractmethod
    def removerConta(ABC):
        pass

    @abstractmethod
    def atualizarConta(ABC):
        pass
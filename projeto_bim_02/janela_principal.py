import tkinter as tk
from janelas.autor.janela_atualizacao import AtualizarAutor_Janela
from janelas.autor.janela_busca import BuscarAutor_Janela
from janelas.autor.janela_cadastro import CadastrarAutor_Janela

from janelas.livro.janela_atualizacao import  AtualizarLivro_Janela
from janelas.livro.janela_busca import BuscarLivro_Janela
from janelas.livro.janela_cadastro import CadastrarLivro_Janela

from janelas.editora.janela_atualizacao import  AtualizarEditora_Janela
from janelas.editora.janela_busca import BuscarEditora_Janela
from janelas.editora.janela_cadastro import CadastrarEditora_Janela

from janelas.funcionario.janela_autenticacao import AutenticarFuncionario_Janela
from janelas.funcionario.janela_cadastro import CadastrarFuncionario_Janela
from janelas.funcionario.janela_remocao_saida import RemoverFuncionario_Janela

from janelas.visitante.janela_autenticacao import AutenticarVisitante_Janela
from janelas.visitante.janela_cadastro import CadastrarVisitante_Janela
from janelas.visitante.janela_remocao_saida import RemoverVisitante_Janela

from janelas.emprestimo.janela_emprestimo import EmprestimoApp

from janelas.exemplar.janela_atualizacao import AtualizarExemplar_Janela
from janelas.exemplar.janela_busca import BuscarExemplar_Janela
from janelas.exemplar.janela_cadastro import CadastrarExemplar_Janela
from janelas.exemplar.janela_remocao import RemoverExemplar_Janela



class JanelaPrincipal:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Biblioteca Hedy Lamarr")
        self.central()

        
        self.menu_bar = tk.Menu(self.janela)
        self.janela.config(menu=self.menu_bar)

        # itens de menu
        menu_livros = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Livros", menu=menu_livros)
        menu_livros.add_command(label="Cadastrar Livro", command=self.janela_cadastro_livro)
        menu_livros.add_command(label="Buscar Livro", command=self.janela_busca_livro)
        
        menu_livros.add_separator()
        menu_livros.add_command(label="Sair", command=self.janela.quit)
        
        menu_editoras = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editoras", menu=menu_editoras)
        menu_editoras.add_command(label="Cadastrar Editora", command=self.janela_cadastro_editora)
        menu_editoras.add_command(label="Buscar Editora", command=self.janela_busca_editora)
        
        menu_autores = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Autores", menu=menu_autores)
        menu_autores.add_command(label="Cadastrar Autor", command=self.janela_cadastro_autor)

        menu_exemplares = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Exemplares", menu=menu_exemplares)
        menu_exemplares.add_command(label="Cadastrar Exemplar", command=self.janela_cadastro_exemplar)
        menu_exemplares.add_command(label="Buscar Exemplar", command=self.janela_busca_exemplar)
        menu_exemplares.add_command(label="Atualizar Exemplar", command=self.janela_atualizacao_exemplar)
        menu_exemplares.add_command(label="Remover Exemplar", command=self.janela_remocao_exemplar)

        menu_emprestimos = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Empréstimos", menu=menu_emprestimos)
        menu_emprestimos.add_command(label="Gerenciar Empréstimos", command=self.janela_emprestimo)


        self.janela.mainloop()


    def central(self):
        largura = 700
        altura = 400
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()

        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)

        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")


    def limpar_widgets(self):
        if len(self.janela.winfo_children()) > 1:
            self.janela.winfo_children()[1].destroy()


    def janela_atualizacao_autor(self):
        self.limpar_widgets()
        AtualizarAutor_Janela(self.janela)


    def janela_cadastro_autor(self):
        self.limpar_widgets()
        CadastrarAutor_Janela(self.janela)

    def janela_busca_autor(self):
        self.limpar_widgets()
        BuscarAutor_Janela(self.janela)


    def janela_atualizacao_livro(self):
        self.limpar_widgets()
        AtualizarLivro_Janela(self.janela)

        
    def janela_cadastro_livro(self):
        self.limpar_widgets()
        CadastrarLivro_Janela(self.janela)

    def janela_busca_livro(self):
        self.limpar_widgets()
        BuscarLivro_Janela
    
    def janela_atualizacao_livro(self):
        self.limpar_widgets()
        BuscarLivro_Janela(self.janela)
    
    def janela_atualizacao_editora(self):
        self.limpar_widgets()
        AtualizarEditora_Janela(self.janela)

        
    def janela_cadastro_editora(self):
        self.limpar_widgets()
        CadastrarEditora_Janela(self.janela)
        
        
    def janela_busca_editora(self):
        self.limpar_widgets()
        BuscarEditora_Janela(self.janela)


    def janela_autenticacao_func(self):
        self.limpar_widgets()
        AutenticarFuncionario_Janela(self.janela)

    def janela_cadastro_func(self):
        self.limpar_widgets()
        CadastrarFuncionario_Janela(self.janela)

    def janela_saida_func(self):
        self.limpar_widgets()
        RemoverFuncionario_Janela(self.janela)


    def janela_autenticacao_vis(self):
        self.limpar_widgets()
        AutenticarVisitante_Janela(self.janela)

    
    def janela_cadastro_vis(self):
        self.limpar_widgets()
        CadastrarVisitante_Janela(self.janela)

    def janela_saida_vis(self):
        self.limpar_widgets()
        RemoverVisitante_Janela(self.janela)

    def janela_cadastro_exemplar(self):
        self.limpar_widgets()
        CadastrarExemplar_Janela(self.janela)

    def janela_busca_exemplar(self):
        self.limpar_widgets()
        BuscarExemplar_Janela(self.janela)

    def janela_atualizacao_exemplar(self):
        self.limpar_widgets()
        AtualizarExemplar_Janela(self.janela)

    def janela_remocao_exemplar(self):
        self.limpar_widgets()
        RemoverExemplar_Janela(self.janela)

    def janela_emprestimo(self):
        self.limpar_widgets()
        EmprestimoApp(self.janela)

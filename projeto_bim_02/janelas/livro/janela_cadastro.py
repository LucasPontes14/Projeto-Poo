import customtkinter as ctk
import manipulacao_arquivos.mani_livros as mal
import utils as ut
from standart.livro import Livro

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CadastrarLivro_Janela:
    def __init__(self, janela):
        self.frame = ctk.CTkFrame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        # Labels e Entradas para todos os campos
        nome_livro = ctk.CTkLabel(self.frame, text="Nome: ")
        nome_livro.grid(row=0, column=0, sticky='E', padx=5, pady=5)
        self.entrada_nome = ctk.CTkEntry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()

        autor_livro = ctk.CTkLabel(self.frame, text="Autor: ")
        autor_livro.grid(row=1, column=0, sticky='E', padx=5, pady=5)
        self.entrada_autor = ctk.CTkEntry(self.frame)
        self.entrada_autor.grid(row=1, column=1, sticky='W', padx=5, pady=5)
        
        data_edicao = ctk.CTkLabel(self.frame, text="Data de Edição: ")
        data_edicao.grid(row=2, column=0, sticky='E', padx=5, pady=5)
        self.entrada_data_edicao = ctk.CTkEntry(self.frame)
        self.entrada_data_edicao.grid(row=2, column=1, sticky='W', padx=5, pady=5)

        formato_livro = ctk.CTkLabel(self.frame, text="Formato: ")
        formato_livro.grid(row=3, column=0, sticky='E', padx=5, pady=5)
        self.entrada_formato = ctk.CTkEntry(self.frame)
        self.entrada_formato.grid(row=3, column=1, sticky='W', padx=5, pady=5)

        editora_livro = ctk.CTkLabel(self.frame, text="Editora: ")
        editora_livro.grid(row=4, column=0, sticky='E', padx=5, pady=5)
        self.entrada_editora = ctk.CTkEntry(self.frame)
        self.entrada_editora.grid(row=4, column=1, sticky='W', padx=5, pady=5)
        
 
        codigo_livro = ctk.CTkLabel(self.frame, text="Código: ")
        codigo_livro.grid(row=5, column=0, sticky='E', padx=5, pady=5)
        self.entrada_codigo = ctk.CTkEntry(self.frame)
        self.entrada_codigo.grid(row=5, column=1, sticky='W', padx=5, pady=5)

       
        botao = ctk.CTkButton(self.frame, text="Salvar", command=self.livro_cadastrar, fg_color="#800020", hover_color="#66001a", corner_radius=5, text_color="#ffffff")
        botao.grid(row=6, column=0, padx=5, pady=5, columnspan=2)

    def clear(self):
        self.entrada_nome.delete(0, "end")
        self.entrada_autor.delete(0, "end")
        self.entrada_data_edicao.delete(0, "end")
        self.entrada_formato.delete(0, "end")
        self.entrada_editora.delete(0, "end")
        self.entrada_codigo.delete(0, "end") 
        self.entrada_nome.focus()

    def livro_cadastrar(self):
        nome = self.entrada_nome.get()
        autor = self.entrada_autor.get()
        data_edicao = self.entrada_data_edicao.get()
        formato = self.entrada_formato.get()
        editora = self.entrada_editora.get()
        codigo = self.entrada_codigo.get()

        novo_livro = Livro(codigo, nome, autor, data_edicao, formato, editora)

        resultado = mal.cadastrarLivros([novo_livro])
        
        ut.exibir_aviso(resultado, "Livro adicionado!", "Não foi possível cadastrar, tente novamente!")
        self.clear()
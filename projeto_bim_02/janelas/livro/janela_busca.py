

import customtkinter as ctk
import manipulacao_arquivos.mani_livros as mal
from janelas.livro.janela_atualizacao import AtualizarLivro_Janela
import utils as ut
from tkinter import messagebox


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class BuscarLivro_Janela:


    def __init__(self, janela):
        self.janela = janela
        self.autor_buscado= None


        self.frame = ctk.CTkFrame(janela, width=700, height=100)
        self.frame.place(relx=0.5, rely=0.5, anchor= ctk.CENTER)

        nome_livro = ctk.CTkLabel(self.frame, text="Nome: ")
        nome_livro.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome_livro = ctk.CTkEntry(self.frame)
        self.entrada_nome_livro.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome_livro.focus()

        self.botao = ctk.CTkButton(self.frame, text="Buscar", command=self.livro_buscar, fg_color="#800020",  hover_color="#66001a", corner_radius=5 ,text_color="#ffffff")
        self.botao.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.nome_resultado = ctk.CTkLabel(self.frame)
        self.nome_resultado.grid(row=2, column=0, sticky='W', padx=5, pady=5, columnspan=2)


        self.botao_para_atualizar = ctk.CTkButton(self.frame, text="Atualizar", command=self.livro_atualizar, state='disabled', fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff")
        self.botao_para_atualizar.grid(row=6, column=0, padx=5, pady=5, sticky='E')
        
        self.botao_para_remover = ctk.CTkButton(self.frame, text="Remover", command=self.livro_remover, state='disabled', fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff")
        self.botao_para_remover.grid(row=6, column=1, padx=5, pady=5, sticky='W')

        self.textos_voltar()

    def textos_voltar(self):
        self.nome_resultado(text="Nome: ")
        

    def clear(self):
        self.entrada_nome_livro.delete(0 ,'end')


    def exibir_resultado(self, resultado):
        self.textos_voltar()
        
        texto_atual = self.nome_resultado.cget("text")
        texto_atual = texto_atual + resultado.nomeLivro
        self.nome_resultado(text=texto_atual)
        


    def configurando_botoes(self):
        self.botao_para_atualizar(state='normal')
        self.botao_para_remover(state='normal')
        

    def livro_atualizar(self):
        if self.livro_buscado:
             AtualizarLivro_Janela(self.janela, self.autor_buscado)
             self.frame.destroy()
    


        
            
    def livro_buscar(self):
        nome = self.entrada_nome_livro.get()
        resultado = mal.buscarLivro(nome)
        if resultado:
            self.livro_buscado = resultado
            self.exibir_resultado(resultado)
            self.configurando_botoes()
        else:
            self.livro_buscado = None
            self.textos_voltar()
            messagebox.showinfo("Não encontrado!", "''Livro'' não foi achado.")

        self.clear()

        
    def livro_remover(self):
       if not self.livro_buscado:
        messagebox.showwarning ("")
        confirmacao = messagebox.askyesno("Deseja remover Livro?", "Realmente quer remover o livro?")
        
        if confirmacao:
            
            resultado = mal.removerLivro(self.autor_buscado.id)
            
           
            ut.exibir_aviso(resultado, "Livro removido!", "Livro não achado, tente novamente.")
            
        
            self.frame.destroy()
    





    
       

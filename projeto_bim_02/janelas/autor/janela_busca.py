
import customtkinter as ctk
import manipulacao_arquivos.mani_autor as maa
from janelas.autor.janela_atualizacao import AtualizarAutor_Janela
import utils as ut
from tkinter import messagebox


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class BuscarAutor_Janela:


    def __init__(self, janela):
        self.janela = janela
        self.autor_buscado= None


        self.frame = ctk.CTkFrame(janela, width=700, height=100)
        self.frame.place(relx=0.5, rely=0.5, anchor= ctk.CENTER)

        nome_autor = ctk.CTkLabel(self.frame, text="Nome: ")
        nome_autor.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome_autor = ctk.CTkEntry(self.frame)
        self.entrada_nome_autor.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome_autor.focus()

        self.botao = ctk.CTkButton(self.frame, text="Buscar", command=self.autor_buscar, fg_color="#800020",  hover_color="#66001a", corner_radius=5 ,text_color="#ffffff")
        self.botao.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.nome_resultado = ctk.CTkLabel(self.frame)
        self.nome_resultado.grid(row=2, column=0, sticky='W', padx=5, pady=5, columnspan=2)


        self.botao_para_atualizar = ctk.CTkButton(self.frame, text="Atualizar", command=self.autor_atualizar, state='disabled', fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff")
        self.botao_para_atualizar.grid(row=6, column=0, padx=5, pady=5, sticky='E')
        
        self.botao_para_remover = ctk.CTkButton(self.frame, text="Remover", command=self.autor_remover, state='disabled', fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff")
        self.botao_para_remover.grid(row=6, column=1, padx=5, pady=5, sticky='W')

        self.textos_voltar()

    def textos_voltar(self):
        self.nome_resultado(text="Nome: ")
        

    def clear(self):
        self.entrada_nome_autor.delete(0 ,'end')


    def exibir_resultado(self, resultado):
        self.textos_voltar()
        
        texto_atual = self.nome_resultado.cget("text")
        texto_atual = texto_atual + resultado.nomeAutor
        self.nome_resultado(text=texto_atual)
        


    def configurando_botoes(self):
        self.botao_para_atualizar(state='normal')
        self.botao_para_remover(state='normal')
        

    def autor_atualizar(self):
        if self.autor_buscado:
             AtualizarAutor_Janela(self.janela, self.autor_buscado)
             self.frame.destroy()
    


        
            
    def autor_buscar(self):
        nome = self.entrada_nome_autor.get()
        resultado = maa.buscarAutores(nome)
        if resultado:
            self.autor_buscado = resultado
            self.exibir_resultado(resultado)
            self.configurando_botoes()
        else:
            self.autor_buscado = None
            self.textos_voltar()
            messagebox.showinfo("Não encontrado!", "''Autor'' não foi achado.")

        self.clear()

        
    def autor_remover(self):
       if not self.autor_buscado:
        messagebox.showwarning ("")
        confirmacao = messagebox.askyesno("Deseja remover autor?", "Realmente quer remover o autor?")
        
        if confirmacao:
            
            resultado = maa.autor_remover(self.autor_buscado.id)
            
           
            ut.exibir_aviso(resultado, "Autor removido!", "Autor não achado, tente novamente.")
            
        
            self.frame.destroy()
    





    
       

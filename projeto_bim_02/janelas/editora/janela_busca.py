

import customtkinter as ctk
import manipulacao_arquivos.mani_editora as mae
from janelas.editora.janela_atualizacao import AtualizarEditora_Janela
import utils as ut
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class BuscarEditora_Janela:


    def __init__(self, janela):
        self.janela = janela
        self.editora_buscada= None


        self.frame = ctk.CTkFrame(janela, width=700, height=100)
        self.frame.place(relx=0.5, rely=0.5, anchor= ctk.CENTER)

        nome_editora = ctk.CTkLabel(self.frame, text="Nome: ")
        nome_editora.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome_editora = ctk.CTkEntry(self.frame)
        self.entrada_nome_editora.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome_editora.focus()

        self.botao = ctk.CTkButton(self.frame, text="Buscar", command=self.editora_buscar, fg_color="#800020",  hover_color="#66001a", corner_radius=5 ,text_color="#ffffff")
        self.botao.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.nome_resultado = ctk.CTkLabel(self.frame)
        self.nome_resultado.grid(row=2, column=0, sticky='W', padx=5, pady=5, columnspan=2)


        self.botao_para_atualizar = ctk.CTkButton(self.frame, text="Atualizar", command=self.editora_atualizar, state='disabled', fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff")
        self.botao_para_atualizar.grid(row=6, column=0, padx=5, pady=5, sticky='E')
        
        self.botao_para_remover = ctk.CTkButton(self.frame, text="Remover", command=self.editora_remover, state='disabled', fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff")
        self.botao_para_remover.grid(row=6, column=1, padx=5, pady=5, sticky='W')

        self.textos_voltar()

    def textos_voltar(self):
        self.nome_resultado(text="Nome: ")
        

    def clear(self):
        self.entrada_nome_editora.delete(0 ,'end')


    def exibir_resultado(self, resultado):
        self.textos_voltar()
        
        texto_atual = self.nome_resultado.cget("text")
        texto_atual = texto_atual + resultado.nomeEditora
        self.nome_resultado(text=texto_atual)
        


    def configurando_botoes(self):
        self.botao_para_atualizar(state='normal')
        self.botao_para_remover(state='normal')
        

    def editora_atualizar(self):
        if self.editora_buscada:
             AtualizarEditora_Janela(self.janela, self.editora_buscada)
             self.frame.destroy()
    


            
    def editora_buscar(self):
        nome = self.entrada_nome_editora.get()
        resultado = mae.buscarEditora(nome)
        if resultado:
            self.editora_buscada = resultado
            self.exibir_resultado(resultado)
            self.configurando_botoes()
        else:
            self.editora_buscada = None
            self.textos_voltar()
            messagebox.showinfo("Não encontrada!", "''Editora'' não foi achada,tente novamente.")

        self.clear()

        
    def editora_remover(self):
       if not self.editora_buscada:
        messagebox.showwarning ("")
        confirmacao = messagebox.askyesno("Deseja remover editora?", "Realmente quer remover o editora?")
        
        if confirmacao:
            
            resultado = mae.removerEditora(self.editora_buscada.id)
            
           
            ut.exibir_aviso(resultado, "Editora removida!", "Editora não achada, tente novamente.")
            
        
            self.frame.destroy()
    





    
       

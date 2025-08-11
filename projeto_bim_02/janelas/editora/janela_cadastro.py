

import customtkinter as ctk
import manipulacao_arquivos.mani_editora as mae
import utils as ut
from standart.editora import Editora

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CadastrarEditora_Janela:
    def __init__(self, janela):
        self.frame = ctk.CTkFrame(janela, width=700, height=100)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        nome_editora = ctk.CTkLabel(self.frame, text="Nome: ")
        nome_editora.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = ctk.CTkEntry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()


    
        botao = ctk.CTkButton(self.frame, text="Salvar", command=self.editora_cadastrar, fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff" )
        botao.grid(row=2, column=0, padx=5, pady=5, columnspan=2)


    def clear(self):
        self.entrada_nome.delete, (0, "end")
        self.entrada_nome.focus()

    def editora_cadastrar(self):
  
        nome = self.entrada_nome.get()
  
        
        nova_editora = Editora(nome)

     
        resultado = mae.cadastrarEditoras(nova_editora)
    

        ut.exibir_aviso(resultado, "Editora adicionado!", "Não foi possível cadatrar, tente novamente! ")
  

        self.clear()
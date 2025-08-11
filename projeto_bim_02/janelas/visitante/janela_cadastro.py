

import customtkinter as ctk
import manipulacao_arquivos.mani_visitante as mav
import utils as ut
from nao_modelos.visitante import Visitante

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



class CadastrarVisitante_Janela:
    def __init__(self, janela):
        self.frame = ctk.CTkFrame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        nome_visitante = ctk.CTkLabel(self.frame, text="Nome: ")
        nome_visitante.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = ctk.CTkEntry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()


        senha_visit = ctk.CTkLabel(self.frame, text="Senha: ", show = "*")
        senha_visit.grid(row=5, column=0, sticky='E', padx=5, pady=5)
        self.entrada_senha = ctk.CTkEntry(self.frame, show ="*")
        self.entrada_senha.grid(row=5, column=1, sticky='W', padx=5, pady=5)

    
        botao = ctk.CTkButton(self.frame, text="Salvar", command=self.visitante_cadastrar, fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff" )
        botao.grid(row=2, column=0, padx=5, pady=5, columnspan=2)


    def clear(self):
        self.entrada_nome.delete, (0, "end")
        self.entrada_senha.delete(0, "end") 
        self.entrada_nome.focus()

    def visitante_cadastrar(self):
  
        nome = self.entrada_nome.get()
  
        
        novo_visitante = Visitante(nome)

     
        resultado = mav.cadastrarVisitantes(novo_visitante)
    

        ut.exibir_aviso(resultado, "Usuário adicionado!", "Não foi possível cadatrar, tente novamente! ")
  

        self.clear()

import customtkinter as ctk
import manipulacao_arquivos.mani_funcionario as maf
import utils as ut
from nao_modelos.funcionario import Funcionario

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



class CadastrarFuncionario_Janela:
    def __init__(self, janela):
        self.frame = ctk.CTkFrame(janela, width=700, height=100)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        nome_funcionario = ctk.CTkLabel(self.frame, text="Nome: ")
        nome_funcionario.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = ctk.CTkEntry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()

        senha_func = ctk.CTkLabel(self.frame, text="Senha: ", show = "*")
        senha_func.grid(row=5, column=0, sticky='E', padx=5, pady=5)
        self.entrada_senha = ctk.CTkEntry(self.frame, show ="*")
        self.entrada_senha.grid(row=5, column=1, sticky='W', padx=5, pady=5)

    
        botao = ctk.CTkButton(self.frame, text="Salvar", command=self.funcionario_cadastrar, fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff" )
        botao.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

        


    def clear(self):
        self.entrada_nome.delete, (0, "end")
        self.entrada_nome.focus()

    def funcionario_cadastrar(self):
  
        nome = self.entrada_nome.get()
  
        
        novo_funcionario = Funcionario(nome)

     
        resultado = maf.cadastrarFuncionarios(novo_funcionario)
    

        ut.exibir_aviso(resultado, "Funcionário adicionado!", "Não foi possível cadatrar, tente novamente! ")
  

        self.clear()
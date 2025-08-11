
import customtkinter as ctk
import manipulacao_arquivos.mani_editora as mae
import utils as ut
from standart.editora import Editora

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AtualizarEditora_Janela:
    
    def __init__(self, janela, editora):
        self.editora = editora
        self.frame = ctk.CTkFrame (janela, width=700, height=100)
        self.frame.place (relx=0.5, rely=0.5, anchor=ctk.CENTER)


        nome_editora = ctk.CTkLabel(self.frame, text="Nome: ")
        nome_editora.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = ctk.CTkEntry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.insert(0, editora.nome)
        self.entrada_nome.focus()

        botao = ctk.CTkButton(self.frame, text="Atualizar", command=self.editora_atualizar, fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff" )
        botao.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

      
    def clear(self):
        self.entrada_nome.delete(0 ,'end')
       



    def editora_atualizar(self):
        
        nome = self.entrada_nome.get()                      
        
        autor_atualizado = Editora(nome, self.editora.id)
        
       
        resultado = mae.atualizarEditoras(autor_atualizado)
    
        
        ut.exibir_aviso(resultado, "Editora atualizada com sucesso!", "Erro ao atualizar Editora.")
        
        self.clear()
        
        self.frame.destroy()
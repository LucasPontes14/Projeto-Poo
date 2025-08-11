import customtkinter as ctk
import manipulacao_arquivos.mani_autor as maa
import utils as ut
from standart.autor import Autor

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AtualizarAutor_Janela:
    
    def __init__(self, janela, autor):
        self.autor = autor
        self.frame = ctk.CTkFrame (janela, width=700, height=100)
        self.frame.place (relx=0.5, rely=0.5, anchor=ctk.CENTER)


        nome_autor = ctk.CTkLabel(self.frame, text="Nome: ")
        nome_autor.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = ctk.CTkEntry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.insert(0, autor.nome)
        self.entrada_nome.focus()

        botao = ctk.CTkButton(self.frame, text="Atualizar", command=self.autor_atualizar, fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff" )
        botao.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

      
    def clear(self):
        self.entrada_nome.delete(0 ,'end')
       



    def autor_atualizar(self):
        
        nome = self.entrada_nome.get()                      
        
        autor_atualizado = Autor(nome, self.autor.id)
        
       
        resultado = maa.autor_atualizar(autor_atualizado)
    
        
        ut.exibir_aviso(resultado, "Autor atualizado com sucesso!", "Erro ao atualizar autor.")
        
        self.clear()
        
        self.frame.destroy()
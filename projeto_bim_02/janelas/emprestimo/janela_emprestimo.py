import customtkinter as ctk
import manipulacao_arquivos.mani_livros as mal
import manipulacao_arquivos.mani_exemplar as mae
from nao_modelos import emprestimo


ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")  

class EmprestimoApp(ctk.CTk):
    def __init__(self):
       

        self.frame = ctk.CTkFrame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.label_livro_id = ctk.CTkLabel(self.frame, text="ID do Livro:")
    
        self.livro_id = ctk.CTkEntry(self.frame)
        self.livro_id.grid(row=0, column=0, sticky='E', padx=5, pady=5)
        self.livro_id.grid(row=2, column=0, sticky='E', padx=5, pady=5)

        self.botao_emprestar = ctk.CTkButton(self.frame, text="Emprestar", command=self.realizar_emprestimo, fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff" )
        self.botao_emprestar.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

      
        self.devolucao_frame = ctk.CTkFrame(self)
        self.devolucao_frame.grid(row=6, column=0, sticky='E', padx=5, pady=5)

        self.exemplar_id = ctk.CTkLabel(self.devolucao_frame, text="ID do Exemplar:")
        self.exemplar_id.grid(row=8, column=0, sticky='E', padx=5, pady=5)
        self.entrada_exemplar_id = ctk.CTkEntry(self.devolucao_frame)
        self.entrada_exemplar_id.grid(row=10, column=0, sticky='E', padx=5, pady=5)

        self.botao_devolver = ctk.CTkButton(self.devolucao_frame, text="Devolver", command=self.realizar_devolucao)
        self.botao_devolver.grid(row=12, column=0, padx=5, pady=5, columnspan=2)

        self.status_label = ctk.CTkLabel(self, text="", text_color="gray")
        self.status_label.grid(row=14, column=0, sticky='E', padx=5, pady=5)

    def realizar_emprestimo(self):
        livro_id = self.livro_id.get().strip()
        if not livro_id:
            self.status_label.configure(text="Por favor, insira o codigo do livro.", text_color="red")
            return

        exemplar_id = emprestimo(livro_id)
        if exemplar_id:
            self.status_label.configure(text=f"Exemplar {exemplar_id} emprestado com sucesso.", text_color="green")
        else:
            self.status_label.configure(text="Falha no empréstimo. Verifique o ID ou disponibilidade.", text_color="red")

    def realizar_devolucao(self):
        exemplar_id = self.exemplar_id.get().strip()
        if not exemplar_id:
            self.status_label.configure(text="Por favor, insira o ID do exemplar.", text_color="red")
            return

        sucesso = devolucao(exemplar_id)
        if sucesso:
            self.status_label.configure(text=f"Exemplar {exemplar_id} devolvido com sucesso.", text_color="green")
        else:
            self.status_label.configure(text="Falha na devolução. Verifique o ID ou status do exemplar.", text_color="red")

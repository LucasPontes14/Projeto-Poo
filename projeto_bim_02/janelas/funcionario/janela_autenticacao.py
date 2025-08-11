
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AutenticarFuncionario_Janela:
    def __init__(self, janela):
        self.frame = ctk.CTkFrame(janela, width=700, height=100)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        nome_funcionario = ctk.CTkLabel(self.frame, text="Nome:")
        nome_funcionario.grid(row=0, column=0, sticky='E', padx=5, pady=5)
        self.entrada_nome = ctk.CTkEntry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()

       
        label_senha = ctk.CTkLabel(self.frame, text="Senha:")
        label_senha.grid(row=1, column=0, sticky='E', padx=5, pady=5)
        self.entrada_senha = ctk.CTkEntry(self.frame, show="*")
        self.entrada_senha.grid(row=1, column=1, sticky='W', padx=5, pady=5)

        
        botao_entrar = ctk.CTkButton(self.frame, text="Entrar", command=self.autenticar)
        botao_entrar.grid(row=2, column=0, columnspan=2, pady=10)

        self.label_msg = ctk.CTkLabel(self.frame, text="")
        self.label_msg.grid(row=3, column=0, columnspan=2)

    def autenticar(self):
        nome = self.entrada_nome.get()
        senha = self.entrada_senha.get()

       
        if self.validar(nome, senha):
            self.label_msg.configure(text="Autenticação realizado com sucesso!", text_color="green")
           
        else:
            self.label_msg.configure(text="Nome ou senha incorretos.", text_color="red")

    def validar(self, nome, senha):
       
        if nome == "admin" and senha == "123":
            return True
        return False


if __name__ == "__main__":

    autenticacao = AutenticarFuncionario_Janela()

    self.clear()
   

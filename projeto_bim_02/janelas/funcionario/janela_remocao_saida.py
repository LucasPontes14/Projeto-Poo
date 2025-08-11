import customtkinter as ctk
import utils as ut
import manipulacao_arquivos.mani_funcionario as maf
import nao_modelos.funcionario as Funcionario

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class RemoverFuncionario_Janela:
    def __init__(self):

        self.nome_func = ctk.CTkLabel(self, text="Nome do Funcionário a Remover:")
        self.nome_func.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = ctk.CTkEntry(self)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()

        self.botao_remover = ctk.CTkButton(self, text="Remover", command=self.executar_remocao, fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff" )
        self.botao_remover.grid(row=2, column=0, padx=5, pady=5, columnspan=2)



    def executar_remocao(self):
        nome = self.entrada_nome.get().strip()
        if nome == "":
           ut.exibir_aviso("Aviso", "Digite o nome do funcionário.")
           return

        removido = removerFuncionarios(nome)
        if removido:
            ut.exibir_aviso("Sucesso", f"Funcionário '{nome}' removido com sucesso.")
        else:
            ut.exibir_aviso("Erro", f"Nenhum funcionário chamado '{nome}' foi encontrado.")


def removerFuncionarios(funcionarioRemover):
    funcionarios = maf.consultarFuncionarios()
    novos_func = Funcionario(nome)
    if len(novos_func) == len(funcionarios):
        return False  
    else:
        maf.salvarFuncionarios(novos_func)
        return True
    



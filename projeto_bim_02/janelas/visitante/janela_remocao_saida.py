import customtkinter as ctk
import utils as ut
import manipulacao_arquivos.mani_visitante as mav
import nao_modelos.visitante as Visitante

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class RemoverVisitante_Janela:
    def __init__(self):

        self.nome_visit = ctk.CTkLabel(self, text="Nome do Visitante a Remover:")
        self.nome_visit.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_nome = ctk.CTkEntry(self)
        self.entrada_nome.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.entrada_nome.focus()

        self.botao_remover = ctk.CTkButton(self, text="Remover", command=self.executar_remocao, fg_color="#800020",  hover_color="#66001a", corner_radius=5, text_color="#ffffff" )
        self.botao_remover.grid(row=2, column=0, padx=5, pady=5, columnspan=2)



    def executar_remocao(self):
        nome = self.entrada_nome.get().strip()
        if nome == "":
           ut.exibir_aviso("Aviso", "Digite o nome do usuario.")
           return

        removido = removerUsuario(nome)
        if removido:
            ut.exibir_aviso("Sucesso", f"Usuario '{nome}' removido com sucesso.")
        else:
            ut.exibir_aviso("Erro", f"Nenhum usuario chamado '{nome}' foi encontrado.")


def removerUsuario(usuarioRemover):
    visitantes = mav.consultarUsuarios()
    novos_visit = Visitante(nome)
    if len(novos_visit) == len(visitantes):
        return False  
    else:
        mav.salvarUsuarios(novos_visit)
        return True
    



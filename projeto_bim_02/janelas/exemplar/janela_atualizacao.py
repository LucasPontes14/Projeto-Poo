import customtkinter as ctk
from standart.exemplar import Exemplar
import manipulacao_arquivos.mani_exemplar as mae
import utils as ut

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AtualizarExemplar_Janela:
    def __init__(self, janela):
        self.frame = ctk.CTkFrame(janela, width=800, height=300)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        # Campo: ID do Exemplar
        label_id = ctk.CTkLabel(self.frame, text="ID do Exemplar:")
        label_id.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entrada_id = ctk.CTkEntry(self.frame)
        self.entrada_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        botao_buscar = ctk.CTkButton(self.frame, text="Buscar", command=self.buscar_exemplar)
        botao_buscar.grid(row=0, column=2, padx=5, pady=5)

        # Campo: Livro ID
        label_livro_id = ctk.CTkLabel(self.frame, text="Livro ID:")
        label_livro_id.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entrada_livro_id = ctk.CTkEntry(self.frame)
        self.entrada_livro_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Campo: Código do Exemplar
        label_codigo = ctk.CTkLabel(self.frame, text="Código do Exemplar:")
        label_codigo.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entrada_codigo = ctk.CTkEntry(self.frame)
        self.entrada_codigo.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Campo: Disponibilidade (checkbox)
        self.check_disponivel = ctk.CTkCheckBox(self.frame, text="Está disponível?")
        self.check_disponivel.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Botão para salvar alterações
        botao_atualizar = ctk.CTkButton(self.frame, text="Salvar Atualização", command=self.atualizar_exemplar)
        botao_atualizar.grid(row=4, column=0, columnspan=3, pady=10)

    def limpar_campos(self):
        self.entrada_livro_id.delete(0, "end")
        self.entrada_codigo.delete(0, "end")
        self.check_disponivel.deselect()

    def buscar_exemplar(self):
        id_exemplar = self.entrada_id.get()

        if not id_exemplar.isdigit():
            ut.exibir_aviso(False, "", "ID inválido.")
            return

        exemplar = mae.buscar_exemplar_por_id(int(id_exemplar))

        if exemplar:
            self.entrada_livro_id.delete(0, "end")
            self.entrada_livro_id.insert(0, str(exemplar.livro_id))

            self.entrada_codigo.delete(0, "end")
            self.entrada_codigo.insert(0, exemplar.codigoExemplar)

            if exemplar.estaDisponivel:
                self.check_disponivel.select()
            else:
                self.check_disponivel.deselect()
        else:
            ut.exibir_aviso(False, "", "Exemplar não encontrado.")

    def atualizar_exemplar(self):
        try:
            id_exemplar = self.entrada_id.get()
            livro_id = self.entrada_livro_id.get()
            codigo = self.entrada_codigo.get()
            disponivel = self.check_disponivel.get()

            if not (id_exemplar.isdigit() and livro_id.isdigit()):
                ut.exibir_aviso(False, "", "ID do exemplar e livro devem ser numéricos.")
                return

            exemplar = Exemplar(
                id=int(id_exemplar),
                livro_id=int(livro_id),
                codigoExemplar=codigo,
                estaDisponivel=bool(disponivel)
            )

            resultado = mae.atualizar_exemplar(exemplar)

            ut.exibir_aviso(resultado, "Exemplar atualizado com sucesso!", "Erro ao atualizar exemplar.")
            self.limpar_campos()
        except Exception as e:
            print(e)
            ut.exibir_aviso(False, "", f"Ocorreu um erro: {e}")

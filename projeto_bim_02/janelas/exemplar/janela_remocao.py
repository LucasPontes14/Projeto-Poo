import customtkinter as ctk
import manipulacao_arquivos.mani_exemplar as mae
import utils as ut

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class RemoverExemplar_Janela:
    def __init__(self, janela):
        self.frame = ctk.CTkFrame(janela, width=700, height=200)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        # Campo: ID do Exemplar
        label_id = ctk.CTkLabel(self.frame, text="ID do Exemplar:")
        label_id.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entrada_id = ctk.CTkEntry(self.frame)
        self.entrada_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Botão de buscar para verificar se o exemplar existe
        botao_buscar = ctk.CTkButton(self.frame, text="Buscar", command=self.buscar_exemplar)
        botao_buscar.grid(row=0, column=2, padx=5, pady=5)

        # Campo para mostrar o livro_id e código (caso o exemplar seja encontrado)
        self.label_info = ctk.CTkLabel(self.frame, text="Informações do Exemplar:")
        self.label_info.grid(row=1, column=0, columnspan=3, padx=5, pady=10)

        self.label_livro_id = ctk.CTkLabel(self.frame, text="Livro ID: ---")
        self.label_livro_id.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.label_codigo = ctk.CTkLabel(self.frame, text="Código do Exemplar: ---")
        self.label_codigo.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        # Botão para remover o exemplar
        botao_remover = ctk.CTkButton(self.frame, text="Remover Exemplar", command=self.remover_exemplar)
        botao_remover.grid(row=4, column=0, columnspan=3, pady=10)

    def limpar_campos(self):
        self.entrada_id.delete(0, "end")
        self.label_livro_id.config(text="Livro ID: ---")
        self.label_codigo.config(text="Código do Exemplar: ---")
        self.label_info.grid_forget()

    def buscar_exemplar(self):
        id_exemplar = self.entrada_id.get()

        if not id_exemplar.isdigit():
            ut.exibir_aviso(False, "", "ID inválido.")
            return

        exemplar = mae.buscar_exemplar_por_id(int(id_exemplar))

        if exemplar:
            self.label_info.grid(row=1, column=0, columnspan=3, padx=5, pady=10)
            self.label_livro_id.config(text=f"Livro ID: {exemplar.livro_id}")
            self.label_codigo.config(text=f"Código do Exemplar: {exemplar.codigoExemplar}")
        else:
            ut.exibir_aviso(False, "", "Exemplar não encontrado.")

    def remover_exemplar(self):
        try:
            id_exemplar = self.entrada_id.get()

            if not id_exemplar.isdigit():
                ut.exibir_aviso(False, "", "ID inválido.")
                return

            confirmacao = ctk.CTkMessagebox.askyesno(
                "Confirmar Remoção",
                f"Você tem certeza que deseja remover o exemplar com ID {id_exemplar}?",
            )

            if confirmacao:
                resultado = mae.remover_exemplar(int(id_exemplar))

                ut.exibir_aviso(resultado, "Exemplar removido com sucesso!", "Erro ao remover exemplar.")
                self.limpar_campos()
        except Exception as e:
            print(e)
            ut.exibir_aviso(False, "", f"Ocorreu um erro: {e}")

import customtkinter as ctk
import manipulacao_arquivos.mani_exemplar as mae
import utils as ut

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class BuscarExemplar_Janela:
    def __init__(self, janela):
        self.frame = ctk.CTkFrame(janela, width=700, height=300)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        # Campo de entrada: ID do exemplar
        label_id = ctk.CTkLabel(self.frame, text="ID do Exemplar:")
        label_id.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.entrada_id = ctk.CTkEntry(self.frame)
        self.entrada_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        botao_buscar = ctk.CTkButton(self.frame, text="Buscar", command=self.buscar_exemplar)
        botao_buscar.grid(row=0, column=2, padx=5, pady=5)

        # Resultados
        self.label_resultado = ctk.CTkLabel(self.frame, text="Resultado da Busca", font=ctk.CTkFont(size=14, weight="bold"))
        self.label_resultado.grid(row=1, column=0, columnspan=3, pady=10)

        self.label_id_resultado = ctk.CTkLabel(self.frame, text="ID: ---")
        self.label_id_resultado.grid(row=2, column=0, columnspan=3, pady=5)

        self.label_livro_id = ctk.CTkLabel(self.frame, text="Livro ID: ---")
        self.label_livro_id.grid(row=3, column=0, columnspan=3, pady=5)

        self.label_codigo = ctk.CTkLabel(self.frame, text="Código do Exemplar: ---")
        self.label_codigo.grid(row=4, column=0, columnspan=3, pady=5)

        self.label_disponivel = ctk.CTkLabel(self.frame, text="Disponível: ---")
        self.label_disponivel.grid(row=5, column=0, columnspan=3, pady=5)

    def limpar_resultado(self):
        self.label_id_resultado.configure(text="ID: ---")
        self.label_livro_id.configure(text="Livro ID: ---")
        self.label_codigo.configure(text="Código do Exemplar: ---")
        self.label_disponivel.configure(text="Disponível: ---")

    def buscar_exemplar(self):
        self.limpar_resultado()

        id_exemplar = self.entrada_id.get()

        if not id_exemplar.isdigit():
            ut.exibir_aviso(False, "", "ID inválido. Deve ser numérico.")
            return

        exemplar = mae.buscar_exemplar_por_id(int(id_exemplar))

        if exemplar:
            self.label_id_resultado.configure(text=f"ID: {exemplar.id}")
            self.label_livro_id.configure(text=f"Livro ID: {exemplar.livro_id}")
            self.label_codigo.configure(text=f"Código do Exemplar: {exemplar.codigoExemplar}")
            disponivel = "Sim" if exemplar.estaDisponivel else "Não"
            self.label_disponivel.configure(text=f"Disponível: {disponivel}")
        else:
            ut.exibir_aviso(False, "", "Exemplar não encontrado.")

import customtkinter as ctk
from standart.exemplar import Exemplar
import manipulacao_arquivos.mani_exemplar as mae
import utils as ut

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CadastrarExemplar_Janela:
    def __init__(self, janela):
        self.frame = ctk.CTkFrame(janela, width=700, height=200)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        # Campo: ID do Livro
        label_livro_id = ctk.CTkLabel(self.frame, text="ID do Livro:")
        label_livro_id.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.entrada_livro_id = ctk.CTkEntry(self.frame)
        self.entrada_livro_id.grid(row=0, column=1, sticky='W', padx=5, pady=5)

        # Campo: Código do Exemplar
        label_codigo = ctk.CTkLabel(self.frame, text="Código do Exemplar:")
        label_codigo.grid(row=1, column=0, sticky='E', padx=5, pady=5)

        self.entrada_codigo = ctk.CTkEntry(self.frame)
        self.entrada_codigo.grid(row=1, column=1, sticky='W', padx=5, pady=5)

        # Botão de salvar
        botao_salvar = ctk.CTkButton(
            self.frame, text="Salvar Exemplar",
            command=self.salvar_exemplar,
            fg_color="#006400", hover_color="#004d00", corner_radius=5
        )
        botao_salvar.grid(row=2, column=0, columnspan=2, pady=10)

    def clear(self):
        self.entrada_livro_id.delete(0, "end")
        self.entrada_codigo.delete(0, "end")
        self.entrada_livro_id.focus()

    def salvar_exemplar(self):
        try:
            livro_id = self.entrada_livro_id.get()
            codigo = self.entrada_codigo.get()

            if not livro_id.isdigit():
                ut.exibir_aviso(False, "", "ID do livro deve ser numérico.")
                return

            if not codigo:
                ut.exibir_aviso(False, "", "Informe o código do exemplar.")
                return

            novo_exemplar = Exemplar(
                livro_id=int(livro_id),
                codigoExemplar=codigo,
                estaDisponivel=True  # Por padrão, o exemplar é criado como disponível
            )

            resultado = mae.adicionar_exemplar(novo_exemplar)

            ut.exibir_aviso(resultado, "Exemplar cadastrado com sucesso!", "Erro ao cadastrar exemplar.")
            self.clear()

        except Exception as e:
            print(e)
            ut.exibir_aviso(False, "", f"Ocorreu um erro: {e}")

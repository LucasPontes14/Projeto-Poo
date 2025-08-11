import json
from standart.livro import Livro
import os
import utils as ut

CAMINHO_ARQUIVO = "dados/livro.json"

def consultarLivros():
    lista_livros = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_livros
        f = open(CAMINHO_ARQUIVO, "r")
        livros = json.load(f)
        for a in livros:
            obj_exemplar = Livro(**a)
            lista_livros.append(obj_exemplar)
        return lista_livros
    except Exception as e:
        print(e)

def cadastrarLivros(lista):
    try:
        livros_existentes = consultarLivros()
        proximo_id = ut.calcular_proximo_id(livros_existentes)
        for i, livro in enumerate(lista):
            livro.id = proximo_id + i
        livros_todos = livros_existentes + lista
        dados = [livro.to_dict() for livro in livros_todos]
        f = open(CAMINHO_ARQUIVO, "w") 
        json.dump(dados, f, indent=4)
        return True
    except Exception as e:
        print(e)
        return False

def salvarLivros(lista):
    try:
        dados = [livro.to_dict() for livro in lista]
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
        return True
    except Exception as e:
        print(e)
        return False

def removerLivro(livroRemover):
    livros = consultarLivros()
    livros_novos = [livro for livro in livros if livro.nomeLivro != livroRemover] 
    if len(livros_novos) == len(livros):
        print(f"Nenhum livro com o título '{livroRemover}' foi encontrado.")
    else:
        salvarLivros(livros_novos)
        print(f"Livro com o título '{livroRemover}' removido.")

def atualizarLivro(titulo_atualizar, novo_titulo=None, novo_autor=None, novo_codigo=None, novo_dataEdicao=None, novo_editora=None, novo_formato=None):
    livros = consultarLivros()
    atualizado = False
    for livro in livros:
        if livro.nomeLivro == titulo_atualizar:
            if novo_titulo:
                livro.nomeLivro = novo_titulo
            if novo_autor:
                livro.autorLivro = novo_autor
            atualizado = True
            if novo_codigo:
                livro.codigoLivro = novo_codigo 
            if novo_dataEdicao:
                livro.dataEdicao = novo_dataEdicao
            if novo_editora:
                livro.editoraLivro = novo_editora
            if novo_formato:
                livro.formato = novo_formato
            break
    if atualizado:
        salvarLivros(livros)
        print(f"Livro com o título '{titulo_atualizar}' atualizado com sucesso.")
    else:
        print(f"Nenhum livro com o título '{titulo_atualizar}' foi encontrado.")
    
def buscarLivro(nomeLivro):
    try: 
        livros = consultarLivros()
        for livro in livros:
            if livro.nomeLivro == nomeLivro:
                return livro
        return None
    except Exception as e:
        print(e)
        return None

def buscarLivroPorId(id):
    livros = consultarLivros()
    for livro in livros:
        if livro.id == id:
            return livro
    return None
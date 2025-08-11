import json 
from standart.autor import Autor
import os
import utils as ut

CAMINHO_ARQUIVO = "dados/autor.json"

def consultarAutores():
    lista_autores = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_autores
        f = open(CAMINHO_ARQUIVO, "r")
        autores = json.load(f)
        f.close()  
        for a in autores:
            obj_autor= Autor(**a)
            lista_autores.append(obj_autor)
        return lista_autores
    except Exception as e:
        print(e)

def cadastrarAutores(lista):
    autores_existentes = consultarAutores()
    proximo_id = ut.calcular_proximo_id(autores_existentes)
    for i, autor in enumerate(lista):
            autor.id = proximo_id + i
    if autores_existentes is None:
        autores_existentes = []
    autores_todos = autores_existentes + lista
    dados = [autor.to_dict() for autor in autores_todos]
    f = open(CAMINHO_ARQUIVO, "w", encoding="utf-8")
    json.dump(dados, f, indent=4, ensure_ascii=False)
    f.close()
    return True

def salvarAutores(lista):
    try:
        dados = [autor.to_dict() for autor in lista]
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
        return True
    except Exception as e:
        print(e)
        return False

def removerAutor(autorRemover):
    autores = consultarAutores()
    livros_novos = [livro for livro in autores if livro.nomeAutor != autorRemover] 
    if len(livros_novos) == len(autores):
        print(f"Nenhum(a) autor(a) com o nome '{autorRemover}' foi encontrado.")
    else:
        salvarAutores(livros_novos)
        print(f"Autor(a) com o nome '{autorRemover}' removido.")

def atualizarAutor(autorAtualizar, novo_nomeAutor=None, novoId=None, novo_emailAutor=None, novos_livrosAutor=None):
    autores = consultarAutores()
    atualizado = False
    for livro in autores:
        if livro.nomeAutor == autorAtualizar:
            if novo_nomeAutor:
                livro.nomeAutor = novo_nomeAutor
            atualizado = True
            if novoId:
                livro.id = novoId 
            if novo_emailAutor:
                livro.emailAutor = novo_emailAutor
            if novos_livrosAutor is not None:
                livro.livrosAutor = novos_livrosAutor
            break
    if atualizado:
        salvarAutores(autores)
        print(f"Autor com o nome '{autorAtualizar}' atualizado com sucesso.")
    else:
        print(f"Nenhum(a) autor(a) com o nome '{autorAtualizar}' foi encontrado.")
    
def adicionarLivroAutor(id_autor, novo_livro):
    autores = consultarAutores()
    atualizado = False
    for autor in autores:
        if autor.id == id_autor:
            autor.livrosAutor.append(novo_livro)
            atualizado = True
            break
    if atualizado:
        salvarAutores(autores)
        print(f"Livro adicionado ao autor de id {id_autor}.")
    else:
        print("Autor não encontrado.")
    
def removerLivroAutor(id_autor, livro_remover):
    autores = consultarAutores()
    atualizado = False
    for autor in autores:
        if autor.id == id_autor:
            autor.livrosAutor.remove(livro_remover)
            atualizado = True
            break
    if atualizado:
        salvarAutores(autores)
        print(f"Livro '{livro_remover}' removido do autor de id {id_autor}.")
    else:
        print("Autor não encontrado ou livro não existe no autor.")

def buscarAutores(nomeAutor):
    try:
        autores = consultarAutores()
        for autor in autores:
            if autor.nomeAutor == nomeAutor:
                return Autor
        return None
    except Exception as e:
        print(e)
        return None
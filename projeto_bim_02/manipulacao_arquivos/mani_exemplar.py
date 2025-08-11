import json
import os
from standart.exemplar import Exemplar
import utils as ut
from manipulacao_arquivos import mani_livros


# indica o caminho do arquivo a ser manipulado
CAMINHO_ARQUIVO = "dados/exemplar.json"

def carregar_exemplares():
    lista_exemplares = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_exemplares
        f = open(CAMINHO_ARQUIVO, "r")
        exemplares = json.load(f)
        for a in exemplares:
            obj_exemplar = Exemplar(**a)
            lista_exemplares.append(obj_exemplar)
        return lista_exemplares
    except Exception as e:
        print(e)
        
def salvar_exemplares(lista):
    try:
        dados = [exemplar.to_dict() for exemplar in lista]
        
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
            
        return True
    except Exception as e:
        print(e)
        return False

def contar_exemplares(livro_id):
    exemplares = carregar_exemplares()
    contador = 0
    for e in exemplares:
        if e.livro_id == livro_id:
            contador = contador + 1
    return contador

def atualizarLivro(livro_atualizado):
    livros = mani_livros.consultarLivros()  # pega lista atual de livros
    for i, l in enumerate(livros):
        if l.id == livro_atualizado.id:
            livros[i] = livro_atualizado
            break
    else:
        livros.append(livro_atualizado)  # se não achou, adiciona novo

    return mani_livros.salvarLivros(livros)


def adicionar_exemplar(exemplar):
    try:
        exemplares = carregar_exemplares()
        proximo_id = ut.calcular_proximo_id(exemplares)
        exemplar.id = proximo_id
        exemplares.append(exemplar)
        
        livro_id = exemplar.livro_id
        livro = mani_livros.buscarLivroPorId(livro_id)
        if livro:
            livro.exemplaresLivro.append(exemplar.id)
            atualizarLivro(livro) 

        return salvar_exemplares(exemplares)
    except Exception as e:
        print(e)
        return None

    
def buscar_exemplar_por_id(id):  
    exemplares = carregar_exemplares()
    for a in exemplares:
        if a.id == id:
            return a
    return None
    
def atualizar_exemplar(exemplar):
    try:
        exemplares = carregar_exemplares()
        for idx, a in enumerate(exemplares):
            if a.id == exemplar.id:
                exemplares[idx] = exemplar
                salvar_exemplares(exemplares)
                return True
    except Exception as e:
        print(e)
        return False
     
def remover_exemplar(id_exemplar):
    try:
        exemplares = carregar_exemplares()
        exemplar_para_remover = None
        exemplaresNovos = []

        for ex in exemplares:
            if ex.id == id_exemplar:
                exemplar_para_remover = ex
            else:
                exemplaresNovos.append(ex)

        if not exemplar_para_remover:
            print("Exemplar não encontrado.")
            return False

        livro_id = exemplar_para_remover.livro_id
        livro = mani_livros.buscarLivroPorId(livro_id)
        if livro and id_exemplar in livro.exemplaresLivro:
            livro.exemplaresLivro.remove(id_exemplar)
            atualizarLivro(livro)

        return salvar_exemplares(exemplaresNovos)

    except Exception as e:
        print(e)
        return False
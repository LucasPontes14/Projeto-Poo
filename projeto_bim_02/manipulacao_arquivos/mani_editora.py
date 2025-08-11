import json
from standart.editora import Editora
import os
import utils as ut

CAMINHO_ARQUIVO = "dados/editora.json"

def consultarEditoras():
    lista_editoras = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_editoras
        f = open(CAMINHO_ARQUIVO, "r")
        editoras = json.load(f)
        f.close()  
        for a in editoras:
            obj_editoras = Editora(**a)
            lista_editoras.append(obj_editoras)
        return lista_editoras
    except Exception as e:
        print(e)

def cadastrarEditoras(lista):
    try:
        editoras_existentes = consultarEditoras()
        proximo_id = ut.calcular_proximo_id(editoras_existentes)
        for i, editora in enumerate(lista):
            editora.id = proximo_id + i
        if editoras_existentes is None:
            editoras_existentes = []
        editoras_todas = editoras_existentes + lista
        dados = [editora.to_dict() for editora in editoras_todas]
        f = open(CAMINHO_ARQUIVO, "w") 
        json.dump(dados, f, indent=4)
        f.close()
        return True
    except Exception as e:
        print(e)
        return False

def salvarEditoras(lista):
    try:
        dados = [editora.to_dict() for editora in lista]
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
        return True
    except Exception as e:
        print(e)
        return False

def removerEditora(editoraRemover):
    editoras = consultarEditoras()
    editoras_novas = [editora for editora in editoras if editora.nomeEditora != editoraRemover] 
    if len(editoras_novas) == len(editoras):
        print(f"Nenhuma editora com o nome '{editoraRemover}' foi encontrado.")
    else:
        salvarEditoras(editoras_novas)
        print(f"Editora com o nome '{editoraRemover}' removido.")


def atualizarEditoras(nomeEditora_atualizar, novo_nomeEditora=None, novo_id=None): 
    editoras = consultarEditoras()
    atualizado = False
    for editora in editoras:
        if editora.nomeEditora == nomeEditora_atualizar: 
            if novo_nomeEditora:
                editora.nomeEditora = novo_nomeEditora
            if novo_id:
                editora.idEditora = novo_id
            atualizado = True
            break
    if atualizado:
        salvarEditoras(editoras)
        print(f"Editora com o nome '{nomeEditora_atualizar}' atualizado com sucesso.")
    else:
        print(f"Nenhum editora com o nome '{nomeEditora_atualizar}' foi encontrado.")
    
def buscarEditora(nomeEditora):
    try: 
        editoras = consultarEditoras()
        for editora in editoras:
            if editora.nomeEditora == nomeEditora:
                return editora
        return None
    except Exception as e:
        print(e)
        return None
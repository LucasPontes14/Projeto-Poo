import json
from nao_modelos.visitante import Visitante
import utils as ut
import os

CAMINHO_ARQUIVO = "dados/visitante.json"

def consultarUsuarios():
    lista_usuarios = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_usuarios
        f = open(CAMINHO_ARQUIVO, "r")
        exemplares = json.load(f)
        for a in exemplares:
            obj_visitante = Visitante(**a)
            lista_usuarios.append(obj_visitante)
        return lista_usuarios
    except Exception as e:
        print(e)

def cadastrarUsuarios(lista):
    try:
        usuarios_existentes = consultarUsuarios()
        proximo_id = ut.calcular_proximo_id(usuarios_existentes)
        for i, visitante in enumerate(lista):
            visitante.id = proximo_id + i
            visitante.estaCadastrado = True
        usuarios_todos = usuarios_existentes + lista
        dados = [usuario.to_dict() for usuario in usuarios_todos]
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
        return True
    except Exception as e:
        print(e)
        return False
    
def salvarUsuarios(lista):
    try:
        dados = [usuario.to_dict() for usuario in lista]
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
        return True
    except Exception as e:
        print(e)
        return False

def removerUsuario(usuarioRemover):
    usuarios = consultarUsuarios()
    usuarios_novos = [usuario for usuario in usuarios if usuario.nomeUsuario != usuarioRemover] 
    if len(usuarios_novos) == len(usuarios):
        print(f"Nenhuma conta com o nome '{usuarioRemover}' foi encontrado.")
    else:
        salvarUsuarios(usuarios_novos)
        print(f"Conta com o nome '{usuarioRemover}' removido.")

def atualizarConta(usuario_atualizar, novo_nomeUsuario = None, nova_senha = None):
    usuarios = consultarUsuarios()
    atualizado = False
    for usuario in usuarios:
        if usuario.nomeUsuario == usuario_atualizar:
            if novo_nomeUsuario:
                usuario.nomeUsuario = novo_nomeUsuario
            if nova_senha:
                usuario.senha = nova_senha
            atualizado = True
            break
    if atualizado:
        cadastrarUsuarios(usuarios)
        print(f"Conta com o nome '{usuario_atualizar}' atualizada com sucesso.")
    else:
        print(f"Conta não atualizada")
    
def autenticarUsuario(nomeUsuario, senha):
    usuarios = consultarUsuarios()
    for usuario in usuarios:
        if usuario.nomeUsuario == nomeUsuario and usuario.senha == senha:
            print(f"Entrada autorizada")
            return usuario
    print(f"Usuario ou senha incorretos")
    return None


import json
from nao_modelos.funcionario import Funcionario
from nao_modelos.funcionario import Funcionario
import utils as ut
import os

CAMINHO_ARQUIVO = "dados/funcionario.json"

def consultarFuncionarios():
    lista_funcionarios = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_funcionarios
        f = open(CAMINHO_ARQUIVO, "r")
        funcionarios = json.load(f)
        f.close()  
        for a in funcionarios:
            obj_funcionarios = Funcionario(**a)
            lista_funcionarios.append(obj_funcionarios)
        return lista_funcionarios
    except Exception as e:
        print(e)

def cadastrarFuncionarios(lista):
    try:
        funcionarios_existentes = consultarFuncionarios()
        proximo_id = ut.calcular_proximo_id(funcionarios_existentes)
        for i, funcionario in enumerate(lista):
            funcionario.id = proximo_id + i
        funcionarios_todos = funcionarios_existentes + lista
        dados = [funcionario.to_dict() for funcionario in funcionarios_todos]
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
        return True
    except Exception as e:
        print(e)
        return False
    
def salvarFuncionarios(lista):
    try:
        dados = [funcionario.to_dict() for funcionario in lista]
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
        f.close()  
        return True
    except Exception as e:
        print(e)
        return False

def removerFuncionarios(funcionarioRemover):
    funcionarios = consultarFuncionarios()
    funcionarios_novos = [funcionario for funcionario in funcionarios if funcionario.nomeFuncionario != funcionarioRemover] 
    if len(funcionarios_novos) == len(funcionarios):
        print(f"Nenhuma conta com o nome '{funcionarioRemover}' foi encontrado.")
    else:
        salvarFuncionarios(funcionarios_novos)
        print(f"Conta com o nome '{funcionarioRemover}' removido.")

def atualizarConta(funcionarioAtualizar, novo_nomeFuncionario = None, nova_senha = None):
    funcionarios = consultarFuncionarios()
    atualizado = False
    for funcionario in funcionarios:
        if funcionario.nomeFuncionario == funcionarioAtualizar:
            if novo_nomeFuncionario:
                funcionario.nomeFuncionario = novo_nomeFuncionario
            if nova_senha:
                funcionario.senha = nova_senha
            atualizado = True
            break
    if atualizado:
        salvarFuncionarios(funcionarios)
        print(f"Conta com o nome '{funcionarioAtualizar}' atualizada com sucesso.")
    else:
        print(f"Conta não atualizada")

def autenticarFuncionario(nomeFuncionario, senha):
    funcionarios = consultarFuncionarios()
    for funcionario in funcionarios:
        if funcionario.nomeFuncionario == nomeFuncionario and funcionario.senha == senha:
            print("Entrada autorizada.")
            return funcionario    
    print("Usuario ou senha incorretos.")
    return None


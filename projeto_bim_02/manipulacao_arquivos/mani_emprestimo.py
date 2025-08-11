from manipulacao_arquivos import mani_livros
from manipulacao_arquivos import mani_exemplar

def emprestimo(livro_id):
    try:
        livro = mani_livros.buscarLivroPorId(livro_id)
        if not livro:
            print("Livro não encontrado.")
            return None
        exemplares = mani_exemplar.carregar_exemplares()
        exemplares_disponiveis = [ex for ex in exemplares if ex.id in livro.exemplaresLivro and ex.estaDisponivel]
        if not exemplares_disponiveis:
            print("Nenhum exemplar disponível para empréstimo.")
            return None
        exemplar = exemplares_disponiveis[0]
        exemplar.estaDisponivel = False
        livro.exemplaresLivro.remove(exemplar.id)
        mani_livros.atualizarLivro(livro)
        mani_exemplar.salvar_exemplares(exemplares)
        print(f"Exemplar {exemplar.id} emprestado com sucesso.")
        return exemplar.id
    except Exception as e:
        print(e)
        return None

def devolucao(exemplar_id):
    try:
        exemplares = mani_exemplar.carregar_exemplares()
        exemplar = None
        for ex in exemplares:
            if ex.id == exemplar_id:
                exemplar = ex
                break
        if not exemplar:
            print("Exemplar não encontrado.")
            return False
        if exemplar.estaDisponivel:
            print("Exemplar já está disponível.")
            return False
        exemplar.estaDisponivel = True
        livro = mani_livros.buscarLivroPorId(exemplar.livro_id)
        if livro:
            if exemplar.id not in livro.exemplaresLivro:
                livro.exemplaresLivro.append(exemplar.id)
                mani_livros.atualizarLivro(livro)
        mani_exemplar.salvar_exemplares(exemplares)
        print(f"Exemplar {exemplar_id} devolvido com sucesso.")
        return True
    except Exception as e:
        print(e)
        return False
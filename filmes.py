filmes = []


def adicionar_filme(titulo, ano, genero, realizador, nota):
    filme = {
        "id": len(filmes) + 1,
        "titulo": titulo,
        "ano": ano,
        "genero": genero,
        "realizador": realizador,
        "nota": nota,
    }
    filmes.append(filme)


def listar_filmes():
    for filme in filmes:
        print(f"ID: {filme['id']}")
        print(f"Título: {filme['titulo']}")
        print(f"Ano: {filme['ano']}")
        print(f"Gênero: {filme['genero']}")
        print(f"Realizador: {filme['realizador']}")
        print(f"Nota: {filme['nota']}")
        print()


print("Filme listado com sucesso.")


def pesquisar_filme(titulo):
    for filme in filmes:
        if filme["titulo"].lower() == titulo.lower():
            return filme
    return None


def atualizar_filme(id, titulo=None, ano=None, genero=None, realizador=None, nota=None):
    for filme in filmes:
        if filme["id"] == id:
            if titulo:
                filme["titulo"] = titulo
            if ano:
                filme["ano"] = ano
            if genero:
                filme["genero"] = genero
            if realizador:
                filme["realizador"] = realizador
            if nota:
                filme["nota"] = nota
            return True
    return False


def remover_filme(id):
    for filme in filmes:
        if filme["id"] == id:
            filmes.remove(filme)
            return True
    return False

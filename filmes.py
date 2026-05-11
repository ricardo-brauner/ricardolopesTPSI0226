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

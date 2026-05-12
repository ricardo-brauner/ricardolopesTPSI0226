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

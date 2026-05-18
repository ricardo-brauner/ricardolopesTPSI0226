import filmes
import ordenacao

while True:
    print()
    print("======================")
    print(" Biblioteca de Filmes")
    print("======================")
    print("1. Adcionar Filmes")
    print("2. Listar Filmes")
    print("3. Pesquisar Filmes")
    print("4. Atualizar Filmes")
    print("5. Remover Filmes")
    print("6. Ordenar Filmes")
    print("7. Sair")
    print()

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            titulo = input("Digite o título do filme: ")
            ano = input("Digite o ano do filme: ")
            genero = input("Digite o gênero do filme: ")
            realizador = input("Digite o realizador do filme: ")
            nota = input("Digite a nota do filme: ")
            filmes.adicionar_filme(titulo, ano, genero, realizador, nota)

        case "2":
            print("Listar Filmes")
            filmes.listar_filmes()

        case "3":
            print("Pesquisar Filmes")
            titulo = input("Digite o título do filme que deseja pesquisar: ")
            filme = filmes.pesquisar_filme(titulo)
            if filme:
                print(f"ID: {filme['id']}")
                print(f"Título: {filme['titulo']}")
                print(f"Ano: {filme['ano']}")
                print(f"Gênero: {filme['genero']}")
                print(f"Realizador: {filme['realizador']}")
                print(f"Nota: {filme['nota']}")
            else:
                print("Filme não encontrado.")

        case "4":
            print("Atualizar Filme")
            id = int(input("Digite o ID do filme que deseja atualizar: "))
            titulo = input("Digite o novo título do filme ou pressione Enter: ")
            ano = input("Digite o novo ano do filme ou pressione Enter: ")
            genero = input("Digite o novo gênero do filme ou pressione Enter: ")
            realizador = input("Digite o novo realizador do filme ou pressione Enter: ")
            nota = input("Digite a nova nota do filme ou pressione Enter: ")
            if filmes.atualizar_filme(id, titulo, ano, genero, realizador, nota):
                print("Filme atualizado com sucesso.")
            else:
                print("Filme não encontrado.")

        case "5":
            print("Remover Filmes")
            id = int(input("Digite o ID do filme que deseja remover: "))
            confirmacao = input("Tem certeza que deseja remover este filme? (s/n): ")
            if confirmacao == "s" or confirmacao == "S":
                if filmes.remover_filme(id):
                    print("Filme removido com sucesso.")
                else:
                    print("Filme não encontrado.")
            else:
                print("Remoção cancelada.")

        case "6":
            print("Ordenar Filmes")
            print("1. Ordenar por título")
            print("2. Ordenar por ano")
            print("3. Ordenar por gênero")
            criterio = input("Escolha o critério de ordenação: ")
            ordem = input("Escolha a ordem de ordenação (crescente/decrescente): ")

            if criterio == "1":
                criterio = "titulo"
            elif criterio == "2":
                criterio = "ano"
            elif criterio == "3":
                criterio = "genero"

            filmes_ordenados = ordenacao.bubble_sort_filmes(
                filmes.filmes, criterio, ordem
            )

            print("Filmes ordenados:")
            for filme in filmes_ordenados:
                print(
                    f"ID: {filme['id']}, Título: {filme['titulo']}, Ano: {filme['ano']}, Gênero: {filme['genero']}, Nota: {filme['nota']}"
                )

        case "7":
            print("Obrigado, até a próxima.")
            break
        case _:
            print("Opção inválida, deve escolher um número de 1 a 7.")
            input("Pressione Enter para tentar novamente.")

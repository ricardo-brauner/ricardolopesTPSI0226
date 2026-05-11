import filmes

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
            print("Adicionar Filmes")
            titulo = input("Digite o título do filme: ")
            ano = input("Digite o ano do filme: ")
            genero = input("Digite o gênero do filme: ")
            realizador = input("Digite o realizador do filme: ")
            nota = input("Digite a nota do filme: ")
            filmes.adicionar_filme(titulo, ano, genero, realizador, nota)
        case "2":
            print("Listar Filmes")
        case "3":
            print("Pesquisar Filmes")
        case "4":
            print("Atualizar Filme")
        case "5":
            print("Remover Filmes")
        case "6":
            print("Ordenar Filmes")
        case "7":
            print("Obrigado, até a próxima.")
            break
        case _:
            print("Opção inválida, deve escolher um número de 1 a 7.")
            input("Pressione Enter para tentar novamente.")

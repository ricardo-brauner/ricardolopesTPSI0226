def bubble_sort_filmes(filmes, criterio):
    while True:
        trocou = False
        for i in range(len(filmes) - 1):
            if filmes[i][criterio] > filmes[i + 1][criterio]:
                filmes[i], filmes[i + 1] = filmes[i + 1], filmes[i]
                trocou = True
        if not trocou:
            break
    return filmes

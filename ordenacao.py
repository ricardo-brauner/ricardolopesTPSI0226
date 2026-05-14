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


def selection_sort_filmes(filmes, criterio):
    for i in range(len(filmes)):
        min_index = i
        for j in range(i + 1, len(filmes)):
            if filmes[j][criterio] < filmes[min_index][criterio]:
                min_index = j
        filmes[i], filmes[min_index] = filmes[min_index], filmes[i]
    return filmes

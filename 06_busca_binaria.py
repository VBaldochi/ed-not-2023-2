def busca_binaria(lista, val):

    ini = 0                  # Inicio da Lista
    fim = len(lista) - 1     # Fim da lista

    while ini <= fim:
        # Calculando o meio da lista
        meio = (ini + fim) // 2     # Divisão inteira

        # Verifica se o valor que esta no meio da lista
        # é igual ao valor de busca. Em caso afirmativo,
        # retornamos a posição do meio, pois o valor de
        # busca foi encontrado
        if val == lista[meio]:
            return meio

        # Senão, se o valor de busca é MENOR do que o valor
        # do meio, reinicia a busca na metade esqueda da lista
        elif val < lista[meio]:
            fim = meio - 1

        # Por fim, se o valor de busca é MAIOR que o valor
        # do meio, reinicia a busca na metade direita da (sub)lista
        else:
            ini = meio + 1

    # Se chegamos ate este ponto, o valor de busca NÂO EXISTE na lista
    return -1

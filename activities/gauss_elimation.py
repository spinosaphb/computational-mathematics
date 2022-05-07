import numpy as np

def find_index(arr: np.ndarray, i) -> np.ndarray:
    """
    Acha a primeira linha abaixo da DP cujo elemento é != 0 
    """
    index = i+1
    for elem in arr[i+1:, i]:
        if elem != 0:
            return index
        index += 1


def swap_row(arr_: np.ndarray, i) -> np.ndarray:
    """
    Troca linhas
    """
    arr = arr_.copy()
    target_index = find_index(arr, i)
    arr[[i, target_index]] = arr[[target_index, i]]
    return arr


def gaus_elimination(arr_):
    """
    Retorna uma matriz triangular
    """
    arr = arr_.copy()
    i = 0
    # Percorrendo a diagonal principal
    while i < arr.shape[0]:
        
        ## cheagando se o elemento da diagonal principal é 0
        if arr[i][i] == 0:
            arr = swap_row(arr, i)
            continue
        
        k = i+1
        # Percorrendo os elementos abaixo do elemento da diagonal principal
        while k < arr.shape[0]:
            factor = arr[k][i] / arr[i][i]
            arr[k] -= factor * arr[i] 
            k += 1 
        i += 1
    return arr
def sum_primary_diagonal (matrix:list[list[int]])->int:

    somma:int = 0
    
    for i in range(len(matrix)):

        somma += matrix[i][i]
    
    somma_2:int = 0
    counter = len(matrix) -1

    return somma


def sum_secondary_diagonal(matrix:list[list[int]])->int:
    
    somma:int = 0
    counter = len(matrix) -1

    for i in range(len(matrix)):

        somma += matrix[i][counter]
        counter -= 1
    
    return somma
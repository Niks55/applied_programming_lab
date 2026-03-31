def matrix_multiply(matrix1, matrix2):
    if len(matrix1)== 0 or len(matrix2)== 0:
        raise ValueError("One or both matrices are empty.")
    
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    if cols_matrix1 != rows_matrix2:
        raise  ValueError("Incompatible dimensions for multiplication.")
        
    for row in matrix1:
        for val in row:
            if type(val) not in (int, float):
                raise TypeError("M1 contains non-numeric values.")
    for row in matrix2:
        for val in row:
            if type(val) not in (int, float):
                raise TypeError("M2 contains non-numeric values.")

    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            total = 0
            for k in range(cols_matrix1):
                total += matrix1[i][k] * matrix2[k][j]
            result[i][j] = total
    return result

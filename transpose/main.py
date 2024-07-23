def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b = []

    for j in range(len(a[0])):
        row = []
        for i in range(len(a)):
            row.append(a[i][j])
        
        b.append(row)

    return b

transpose_matrix([[1,2,3],[4,5,6]])

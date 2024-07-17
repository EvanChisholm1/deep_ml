def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    out = []
    for row in a:
        dot_prod = 0
        if not len(row) == len(b): return -1
        for i in range(len(row)):
            dot_prod += row[i] * b[i]
        
        out.append(dot_prod)
    return out

print(matrix_dot_vector([[1,2], [2,4]], [1,2]))

def get_matrix(n,m, value):
    matrix = []
    for i in range(0, n):
        mat_1 = []
        for k in range(0, m):
            mat_1.append(value)
        matrix.append(mat_1)
    return matrix

rez_1 = get_matrix(2,4,3)
rez_2 = get_matrix(5, 6, 4)
rez_3 = get_matrix(3, 8,5)

print(rez_1)
print(rez_2)
print(rez_3)
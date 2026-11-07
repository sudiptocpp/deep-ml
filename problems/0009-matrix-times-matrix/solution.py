def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b): return -1
    k = len(b)
    c = [[0]*(len(b[0])) for _ in range(len(a))]
    for ki in range(k):
        for i in range(len(a)):
            for j in range(len(b[0])):
                c[i][j] += a[i][ki]*b[ki][j]

    return c
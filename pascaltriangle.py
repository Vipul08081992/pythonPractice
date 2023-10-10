def ptriangle(n):
    a = [[0 for j in range(i + 1)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                a[i][0] = 1
            elif j == i:
                a[i][i] = 1
            else:
                a[i][j] = a[i - 1][j-1] + a[i - 1][j]

    for i in range(n):
        for j in range(i + 1):
            print(a[i][j], end=" ")
        print()

ptriangle(6)
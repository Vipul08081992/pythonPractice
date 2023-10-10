X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
sum= [[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]

for i in range(3):
        for j in range(3):
            sum[i][j] = X[i][j] + Y[i][j]
print("result matrix:")
for i in range(3):
        for j in range(3):
            print(sum[i][j],end=" ")
        print()



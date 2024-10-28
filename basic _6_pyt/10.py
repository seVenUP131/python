from random import randint
m=5; n=7
A = [[randint(0,10) for _ in ' '*n] for _ in ' '*m]
print(*A,sep='\n')
print()
 
l=3
for i in range(m):
    for j in range(n):
        if j!=l: A[i][j]*=A[i][l]
 
print(*A,sep='\n')
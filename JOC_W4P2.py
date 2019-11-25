#You are provided with the number of rows (R) and columns (C). 
#Your task is to generate the matrix having R rows and C columns such that all the numbers are in increasing order starting from 1 in row wise manner.

r,c=map(int,input().split())

matrix=[]
h=1

for _ in range(r):
    new_l=[]
    for i in range(c):
        new_l.append(h)
        h+=1
    
   
    matrix.append(new_l)
    
for i in range(r):
    if i == r-1:
        print(*matrix[i],end="")
    else:
        print(*matrix[i])
    

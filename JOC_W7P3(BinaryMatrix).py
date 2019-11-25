"""Given a matrix with N rows and M columns, the task is to check if the matrix is a Binary Matrix. A binary matrix is a matrix in which all the elements are either 0 or 1.

Input Format:
The first line of the input contains two integer number N and M which represents the number of rows and the number of columns respectively, separated by a space.
From the second line, take N lines input with each line containing M integer elements with each element separated by a space. 

Output Format:
Print 'YES' or 'NO' accordingly"""

r,c=map(int,input().split())
matrix=[]
for i in range(r):
    new_l=[int(x) for x in input().split()]
    matrix.append(new_l)
h=0
for i in range(c):
    for j in range(r):
        if matrix[j][i]>1:
            h+=1
        else:
            pass
if h>0:
    print("NO",end="")
else:
    print("YES",end="")

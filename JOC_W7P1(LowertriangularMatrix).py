"""A Lower triangular matrix is a square matrix (where the number of rows and columns are equal)  where all the elements above the diagonal are zero.
For example, the following is an upper triangular matrix with the number of rows and columns equal to 3.

1 0 0
4 5 0
7 8 9

Write a program to convert a square matrix into a lower triangular matrix."""

h=int(input())
l=[]
for i in range(h):
    new_l=[int(x)for x in input().split()]
    l.append(new_l)

s=int(len(l[0]))    

for i in range(int(len(l))):

    if s>0:
        for j in range(1,s):
            l[i][-j]=0
    s-=1

for i in range(len(l)):
    
    if i==int(len(l))-1:
        print(*l[i],end="")
    else:
        print(*l[i])

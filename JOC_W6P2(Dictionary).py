"""Given a positive integer number n, you have to write a program that generates a dictionary d which contains (i, i*i*i) such that i is the key and i*i*i is its value, where i is from 1 to n (both included).
Then you have to just print this dictionary d."""

dic={}
n=int(input())
for i in range(1,n+1):
    dic[i]=i**3
print(dic,end="")

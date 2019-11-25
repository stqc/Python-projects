"""Given an integer number n, define a function named printDict() which can print a dictionary where the keys are numbers between 1 and n (both included) and the values are square of keys.
The function printDict() doesn't take any argument"""

def printDict():
    dic={}
    n=int(input())
    for i in range(1,n+1):
        dic[i]=i**2
    return print(dic,end="")
 
printDict()

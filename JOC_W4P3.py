#You all have used the random library of python. You have seen in the screen-cast of how powerful it is.
"""In this assignment, you will sort a list let's say list_1 of numbers in increasing order using the random library.

Following are the steps to sort the numbers using the random library.

Step 1: Import the randint definition of the random library of python. Check this page if you want some help.

Step 2: Take the elements of the list_1 as input.

Step 3: randomly choose two indexes i and j within the range of the size of list_1.

Step 4: Swap the elements present at the indexes i and j. After doing this, check whether the list_1 is sorted or not.

Step 5: Repeat step 3 and 4 until the array is not sorted."""

from random import randint

n=int(input())
new_list=[]
for _ in range(n):
    new_list.append(input())
h=list(new_list)    
h.sort()

while new_list!=h:
    i=randint(0,int(len(h))-1)
    j=randint(0,int(len(h))-1)
    temp=new_list[i]
    new_list[i]=new_list[j]
    new_list[j]=temp
    
print(*new_list,end="")

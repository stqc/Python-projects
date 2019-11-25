"""Given a list A of n elements, representing the marks. There are m students and you have to distribute the marks from the list A to m students such that:

1) Each student gets marks.
2) The difference between the maximum marks and minimum marks given to the students is minimised.

Input Format:
The first line contains the value n and m respectively separated by a space.
The second line contains the elements of list A separated by a space

Output Format:
Print the minimum difference"""

m,n=input().split()

s=[int(x) for x in input().split()]
s.sort()

i=0
j=i+int(n)-1

smallest=s[j]-s[i]

while j<len(s):
    if s[j]-s[i]<smallest:
        smallest=s[j]-s[i]
    i+=1
    j+=1
    
    if(j==len(s)):
        break

print(smallest,end='')

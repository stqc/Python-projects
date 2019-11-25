"""With a given list L of integers, write a program to print this list L after removing all duplicate values with original order preserved.

Example:

If the input list is

12 24 35 24 88 120 155 88 120 155

Then the output should be

12 24 35 88 120 155
"""

l=[int(x) for x in input().split()]
s=[]

for i in range(int(len(l))):
  if l[i] not in  s:
    s.append(l[i])
print(*s,end="")

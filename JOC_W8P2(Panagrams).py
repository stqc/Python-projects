"""A panagram is a sentence containing every 26 letters in the English alphabet. Given a string S, check if it is panagram or not.

Input Format:
The first line contains the sentence S.

Output Format:
Print 'YES' or 'NO' accordingly"""

from string import ascii_lowercase as asc
l=list(asc)
s="YES"
p=input()
for i in range(int(len(l))):
    if l[i] not in p.lower():
        s="NO"
        break
    else:
        pass
print(s,end="")

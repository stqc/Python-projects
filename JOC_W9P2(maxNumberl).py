"""Given an alphanumeric string S, extract maximum numeric value from that string. All the alphabets are in lower case. Take the maximum consecutive digits as a single number.

Input Format:
The first line contains the string S.

Output Format:
Print the maximum value"""

s=input()
l=[]
for i in s:
    l.append(i)
s=[]
for i in range(int(len(l))-1):
    if l[i].isnumeric() == True and l[i+1].isnumeric() == True:
        l[i+1]=l[i]+l[i+1]
for i in range(len(l)):
    if l[i].isdigit()==True:
            s.append(int(l[i]))
print(max(s),end="")

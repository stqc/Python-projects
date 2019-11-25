#You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.

number=input()
new_list=[]
for i in number:
    new_list.append(i)

zero=new_list.count("0")
one=new_list.count("1")

if int(len(new_list))==2 and zero-one==0 :
    print("YES",end="")
elif int(len(new_list))>2 and zero-one==zero-1 or one-zero==one-1:
    print("YES",end="")
else:
    print("NO",end="")

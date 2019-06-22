a_list=[55,4,65,34,1,98]
sorted=False
s_list=[]
while sorted==False:
    s=a_list[0]
    for i in range(len(a_list)):
        if s>a_list[i]:
            s=a_list[i]
    a_list.remove(s)
    s_list.append(s)
    if len(a_list)==0:
        print(s_list)
        sorted=True
    

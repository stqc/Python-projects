def sorter(a_list):
  j=0 
  while j!=len(a_list): #loop runs while the j is not equal to the length of a_list
      for i in range(len(a_list)): #a second loop to iterate through all the elements of a_list
#if the element of a_list a the i'th position is greater than the element of the a_list at j'th position then these elements are swapped
          if a_list[i]>a_list[j]: 
              temp=a_list[i]
              a_list[i]=a_list[j]
              a_list[j]=temp

      j+=1
      print('------------')
      print(a_list)
a_list=[55,4,65,34,1,98,100,99,67]
sorter(a_list) #sorter function called

"""A semiprime number is an integer which can be expressed as a product of two distinct primes. For example 15 = 3*5 is a semiprime number but 9 = 3*3 is not .
Given an integer number N, find whether it can be expressed as a sum of two semi-primes or not (not necessarily distinct)."""

x=int(input())
prime=[]
semi_prime=[]
result=[]
for i in range(2,x+1):
        r=0
        for j in range(2,x+1):
             if i%j==0:
                    
                    r+=1
        if r==1:
            prime.append(i)
        
for i in range(int(len(prime))):
        for j in range(int(len(prime))):
            if(prime[i]==prime[j]):
                pass
            else:
               
                semi_prime.append(prime[i]*prime[j])
    
semi_prime=set(semi_prime)
semi_prime=list(semi_prime)
    
for i in range(int(len(semi_prime))):
        for j in range(int(len(semi_prime))):
            result.append(semi_prime[i]+semi_prime[j])
result=set(result)
    
if x in result:
        print("Yes",end="")
else:
        print("No",end="")

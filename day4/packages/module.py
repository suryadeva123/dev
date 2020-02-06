def add(a,b):
     return(a+b)
    
def isleapyear(year):
    if (year%400 == 0) or (year%4 == 0 and year%100!=0):
        print("isleapyear")
    else:
        print("is notleapyear")
        
def isprime(num):
    flag = 0
    for i in range(2,num):
        if num%i == 0:
            flag = 1
    if flag == 1:
        print("not a prime")
    else:
        print("prime")
        
def allEven(lb,ub):
    for i in range(lb,ub+1):
        if i%2 == 0:
            print(i)
        
def fact(number):
    mul =1
    for i in range(1,number+1):
        mul *= i
    return mul
        
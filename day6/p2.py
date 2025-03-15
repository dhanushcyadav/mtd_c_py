from math import sqrt
num1 = int(input("enter the input number"))
num2 = int(input("enter the input number"))

for i in range(num1,num2+1):
    for j in range(1,int(sqrt(i))+1):
        if i % j == 0:
            list_of_primes.
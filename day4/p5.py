#program to print the numbers and from m to n (m<n) with an increment of p

m = int(input('enter the M value(start value): '))
n = int(input('enter the N value(end value): '))
p = int(input('enter the P value(increment): '))


i = m
while(i<=n):
    print(i,end = ' ')
    i = i + p


else:
    print('mostly you gave the value to M which is bigger than N')
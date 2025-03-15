n, p = map(int,input("Enter n and p respectively").split())
prices = list(map(int,input('Enter the shoe prices').split()))
sum = 0
prices.sort()
for i in range(0,p):
    if prices[i] < 0:
        sum += prices[i]
print(sum)
import sys
n = int(input("Enter the number of oranges plucked: "))
diameter_of_oranges = list(map(int,input(f"Enter diameter of {n} oranges: ").split()))
reference_orange_diameter = diameter_of_oranges[-1]
if len(diameter_of_oranges) != n:
    print("The number of oranges doesn't match the number of diameter of oranges entered")
    sys.exit()
oranges_big = []
oranges_small = []
number_of_references = 0
for i in range(n):
    if diameter_of_oranges[i] < reference_orange_diameter:
        oranges_small.append(diameter_of_oranges[i])
    elif diameter_of_oranges[i] > reference_orange_diameter:
        oranges_big.append(diameter_of_oranges[i])
    else:
        number_of_references += 1
oranges_sold = oranges_small + [reference_orange_diameter] * number_of_references + oranges_big
print(f"Diameter of oranges sold: {oranges_sold}")

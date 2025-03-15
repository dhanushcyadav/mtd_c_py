#axxept a number and find its and square root
import math
print('enter a number to find its root')
input_number = int(input())                   #input number always returns a string


root_number  = math.sqrt(input_number)
print('sqaure root of' ,input_number,'is'+ str (root_number))        #in python theres no implicit type casting

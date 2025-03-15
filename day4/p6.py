my_name  = 'dhanush'

print(my_name)
print(my_name.upper())
try:
    print(my_name.index('dh'))
except ValueError:
    print(f'the substring \'dh\' not found in {my_name} ')
print(my_name.capitalize())
print(my_name.find('dh'))

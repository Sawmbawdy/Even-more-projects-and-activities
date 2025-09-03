def factorial(x):
    '''This is a recursive function'''
    if int(x) == 0 or int(x) == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial.__doc__)
print("5 -- ", factorial(5))
print("10 --", factorial(10))
print("7 --", factorial(7))

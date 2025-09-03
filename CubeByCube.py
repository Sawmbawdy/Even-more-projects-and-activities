def cube(numb):
    return numb*numb*numb

def by_three(num):
    if num%3 == 0:
        return cube(num)
    else:
        return False
    
print(by_three(3))
print(by_three(13))
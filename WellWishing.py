def add(num1, num2):
    print("Number 1 is", num1)
    print("Number 2 is", num2)
    return num1 + num2

input1 = int(input("Enter the first number: \n"))
input2 = int(input("Enter the second number: \n"))
result = add(input1, input2)
print("The sum is", result)
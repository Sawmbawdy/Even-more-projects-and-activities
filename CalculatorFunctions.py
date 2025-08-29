def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q    
def multiply(P,Q):
    return P * Q
def divide(P,Q):
    return P / Q
def square(P):
    return P ** Q

P = int(input("Enter the first number: \n"))
Q = int(input("Enter the second number: \n"))

print("a - addition")
print("b - subtraction")
print("c - multiplication")
print("d - division")
print("e - square and above")
operation = input("Choose the operation you want to perform: \n").lower()

if operation == "a":
    print(P, "+", Q, "=", add(P,Q))
elif operation == "b":
    print(P, "-", Q, "=", subtract(P,Q))
elif operation == "c":
    print(P, "*", Q, "=", multiply(P,Q))
elif operation == "d":
    print(P, "/", Q, "=", divide(P,Q))
elif operation == "e":
    print(P, "^", Q, "=", square(P))
else:
    print("Invalid Input")
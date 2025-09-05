

condition = str(input("Shutdown program? \n"))

def Shutdown():
    if condition == "yes":
        print("Shutting down")
    elif condition == "no":
        print("abort shutdown")
    else:
        print("sorry, couldn't understand")

Shutdown()
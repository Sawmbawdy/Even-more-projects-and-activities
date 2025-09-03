def total_calc(bill, perc):
    total = bill * (perc * 0.01)
    total = round(total, 2)
    print("Tip =", total)

inpu1 = float(input("What is your total bill \n"))
inpu2 = float(input("How much do you want to tip \n"))

total_calc(inpu1, inpu2)

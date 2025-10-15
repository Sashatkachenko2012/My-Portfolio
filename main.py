time = int(input("How many years are you training in this gym?"))
cost = float(input("How much are you paying?"))

if time > 1 :
    discount = cost * 0.10
else :
    discount = cost

print (f"Your discount for the next month is ${discount}")
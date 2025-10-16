import math

r = float(input("What is the radius of your circle "))

def circle_calculation_area(r): 
    area = math.pi * (r ** 2 )
    return area

if r < 0 :
    print("The radius must be more than 0 ")
else:
    result= circle_calculation_area(r)

    
    print(f"The area is {result}")
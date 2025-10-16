import math
radius = float(input("What is the radius of your circle"))

if radius < 0 :
    print("the radius must be more than 0")
else :
    area = math.pi * (radius ** 2)

    print(f"the area is {area}")



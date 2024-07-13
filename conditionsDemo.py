#if-else
# multi line comment
'''
x=int(input("Enter No1:"))
y=int(input("Enter No2:"))
if x>y :#if block starts
    print(f"{x} is largest")
elif x==y:
    print("Both values are same")
else:
    print(f"{y} is largest")
'''
# you have 3 sides , if they forms a traingle which traingle is it?
#equilateral / isoceles / scalene
'''
x=int(input("Enter Side1:"))
y=int(input("Enter Side2:"))
z=int(input("Enter Side3:"))

if x+y>z and y+z>x and z+x>y:
    if x==y and y==z:
        print("Equilateral Traingle")
    elif x==y or y==z or z==x:
        print("Isoceles Traingle")
    else:
        print("Scalene Traingle")
else:
    print("Invalid Sides")
'''
choice = int(input(
'''
Press 1 for Pizza
Press 2 for Burger
Press 3 for Desert
Press 4 for Cold Drink
'''
))

match choice:
    case 1:print("Your Pizza is Ready")
    case 2:print("Your Burger is Ready")
    case 3:print("Your Ice Cream is Ready")
    case 4:print("Your Coke is Ready")
    case _:print("Invalid Input") 

#Write a program that accepts the lengths of three sides of a triangle as inputs. 
#The program output should indicate whether or not the triangle is a right triangle.

print("Enter the length of Hypotenuse : ")
Hypotenuse=int(input())
print("Enter the length of Perpendicular : ")
Perpendicular =int(input())
print("Enter the length of Base : ")
Base=int(input())
print("To check whether the triangle is a right triangle or not")
if Hypotenuse**2 == Perpendicular**2 + Base**2:
    print("It is a Right Triangle")
else:
    print("It is not a Right Triangle")



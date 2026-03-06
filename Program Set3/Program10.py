# WAP to calculate area and perimeter of different geometrical shapes.


print("---- Select Geometrical Shape ----")
print("1. Rhombus")
print("2. Isosceles Triangle")
print("3. Right Angle Triangle")
print("4. Parallelogram")

choice = int(input("Enter your choice: "))

if choice == 1:
    l = float(input("Enter side of rhombus: "))
    d1 = float(input("Enter first diagonal: "))
    d2 = float(input("Enter second diagonal: "))
    perimeter = 4 * l
    area = (d1 * d2) / 2
    print("Perimeter of rhombus:", perimeter)
    print("Area of rhombus:", area)

elif choice == 2:
    s = float(input("Enter equal side: "))
    b = float(input("Enter base: "))
    perimeter = 2 * s + b
    area = (b / 2) * ((s**2 - (b**2 / 4)) ** 0.5)
    print("Perimeter of isosceles triangle:", perimeter)
    print("Area of isosceles triangle:", area)

elif choice == 3:
    b = float(input("Enter base: "))
    p = float(input("Enter perpendicular: "))
    h = float(input("Enter hypotenuse: "))
    area = 0.5 * b * p
    perimeter = b + p + h
    print("Area of right angle triangle:", area)
    print("Perimeter of right angle triangle:", perimeter)

elif choice == 4:
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    perimeter = 2 * (a + b)
    print("Perimeter of parallelogram:", perimeter)

else:
    print("Invalid choice")

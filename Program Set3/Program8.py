# WAP to calculate the area and perimeter of a right angle triangle

class rat:
    def __init__(self):
        h=float(input("Enter the value of hypotenuse"))
        p=float(input("Enter the value of perpendicular"))
        b=float(input("Enter the value of base"))
        self.h=h
        self.p=p
        self.b=b
    def arearat(self):
        area= 1/2*(self.p*self.b)
        print("Area of right angle triangle is:",area)
    def perimeterrat(self):
        perimeter= (self.b+self.p+self.h)
        print("Perimeter of right angle triangle is:",perimeter)
rt=rat()
rt.arearat()
rt.perimeterrat()        
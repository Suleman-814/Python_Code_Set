# WAP to calculate the perimeter and area of an isosceles triangle

class isosceles:
    def __init__(self):
        print("Two values taken as in isosceles triangle two sides have same values and one side is unequal value")
        s12= float(input("Enter the value of sides which is equal"))
        b1= float(input("Enter the value of unequal side"))
        self.s12=s12
        self.b1=b1
    def perimeterisosceles(self):
        perimeter= 2*self.s12+self.b1
        print("Perimeter of isosceles triangle is :", perimeter)
    def areaisosceles(self):
        area= self.b1/2*(self.s12**2-self.b1**2/4)**0.5
        print("Area of isosceles triangle is:",area)
iso=isosceles()
iso.perimeterisosceles()
iso.areaisosceles()
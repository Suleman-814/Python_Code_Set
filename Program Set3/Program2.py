# WAP to calculate the area and perimeter of a square using a class.
class square:
    def __init__(self):
        s= float(input("Enter the side of square"))
        self.s = s
       
    def areaofsquare(self):
        area= (self.s**2)
        print(f"Area of side of square {self.s}  is:",area)
    def perimeter(self):
        perimeter= 4*self.s
        print(f"Perimeter of side of square {self.s} is:",perimeter)
y=square()
y.areaofsquare()
y.perimeter()
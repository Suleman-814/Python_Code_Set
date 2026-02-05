# WAP to calculate the area and perimeter of a rectangle using a class


class rectangle:
    def __init__ (self):
        a= float(input("Enter length of rectangle"))
        b= float(input("Enter breadth of rectangle"))
        self.a = a
        self.b = b

    def areaofrec(self):
        area = (self.a*self.b)
        print(f"area of {self.a} and {self.b} is:",area,"cm")
    def per(self):
        perimeter= 2*(self.a+self.b)
        print(f"Perimeter of {self.a} and {self.b} is:",perimeter)
x= rectangle()
x.areaofrec()
x.per()
# WAP to calculate the area and perimeter of an equilateral triangle using a class.

class equilateral:
    def __init__(self):
        print("Taken only one side as equilateral triangle as all sides equal, So Enter the side of equilateral triangle")
        side= float(input("Enter a side of equilateral Triangle:"))
        self.side=side
    
    def perimeterequilateral(self):
        per= 3*self.side
        print("Perimeter of equlateral triangle is:",per)
    def areaequilateral(self):
        area= (3)**0.5/4*self.side**2
        print(area)
x= equilateral()
x.perimeterequilateral()
x.areaequilateral()
    
    
    
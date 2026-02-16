# WAP to calculate the area and circumference of a circle using a class.


class circle:
    def __init__(self):
        r=float(input("Enter the radius of circle:"))
        self.r=r
    def areaofcircle(self):
        area= 3.14*self.r**2
        print(f"Area of circle of radius {self.r} is:",area)
    def circumferenceorperimeter(self):
        perimeter= 2*3.14*self.r
        print(f"Perimeter or Circumference of radius {self.r} is:",perimeter)
y=circle()
y.areaofcircle()
y.circumferenceorperimeter()
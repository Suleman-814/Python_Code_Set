# WAP to calculate the area and perimeter of a scalene triangle using a class.

class scalene:
    def __init__(self):
        s1=float(input("Enter the 1st side of scalene triangle:"))
        s2=float(input("Enter the 2nd side or base of scalene triangle:"))
        s3=float(input("Enter the 3rd side of scalene triangle:"))
        self.s1=s1
        self.s2=s2
        self.s3=s3
        if self.s1==self.s2==self.s3:
            print("This is not scalene triangle, all sides cannot be same in scalene triangle")
            return
        elif self.s1==self.s2:
            print("Not a scalene triangle")
            return
        elif self.s1==self.s3:
            print("Not a scalene triangle")
            return
        elif self.s2==self.s3:
            print("Not a scalene triangle")
            return
        
        
    def perimeterscalen(self):
        if self.s1!=self.s2 and self.s1!=self.s3 and self.s2!=self.s3:
            perimeter=(self.s1+self.s2+self.s3)
            print(f"Perimeter of scalene triangle is:", perimeter)
    def area(self):
        s= (self.s1+self.s2+self.s3)/2
        print("semi perimeter of scalene triangle is:",s)
        print("To find area of scalene triangle we use Heron's Formula")
        area= (s*(s-self.s1)*(s-self.s2)*(s-self.s3))**0.5
        print("Area of Scalene triangle is",area,"cm²")
               
      
            
x= scalene()
x.perimeterscalen()
x.area()
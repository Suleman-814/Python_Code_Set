# WAP to calculate the perimeter and area of a rhombus

class rhombus:
    def __init__(self):
        l=float(input("Enter a length of rhombus:"))
        self.l=l
    
    def perimeterofrhombus(self):
        perimeter= 4*self.l
        print("Perimeter of rhombus is:",perimeter)
    def areaofrhombus(self):
        d=str(input("Is both diagonal given Yes or No:"))
        if d== "yes":
            d5=d.lower()
            d1= float(input("Enter the length of diagonal(d1):"))
            d2= float(input("Enter the length of diagonal(d2):"))
            self.d1=d1
            self.d2=d2
            area= (self.d1*self.d2)/2
            print("Area of rhombus is :", area)  
            return
        if d== "no":
            d5=d.lower()
            h1=str(input("Is height is given Yes or No"))
            h2=h1.lower()
            if h1=="Yes" or "yes":
                h3=float(input("Enter the height of rhombus"))
                area2= self.l*h3
                print("Area of rhombus is:", area2)                  
x=rhombus()
x.perimeterofrhombus()
x.areaofrhombus()


             
        
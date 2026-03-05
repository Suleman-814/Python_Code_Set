# WAP to calculate the perimeter of a parallelogram

class parallelogram:
    def __init__(self):
        print("We know that opposite of parallelogram are parallel and equal to each other")
        a= int(input("Enter the value of parallelogram which have same values (first whose values are same)"))
        b= int(input("Enter the value of parallelogram which have same values (second whose values are same)"))
        self.a=a
        self.b=b
    def perimeterparallelogram(self):
        perimeter= (2*self.a+2*self.b)
        print("Perimeter of parallelogram is:",perimeter)
ppl=parallelogram()
ppl.perimeterparallelogram()
        
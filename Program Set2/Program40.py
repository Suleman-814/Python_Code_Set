#WAP to find a square of a number.

def square():
    num1= int(input("Enter a number:"))
    num2= int(input("Enter a number:"))
    listnum=[]
    for i in range (num1, num2):
      
        square= i**2
        print(i, square)
square()
        
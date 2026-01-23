#WAP to finf the power of a number(exponentiation).

def expo():
    b= int(input("Enter a  base nuber"))
    p= int(input("Enter a  power nuber"))
    a= b**p
    print(a)
    if b<0 and p<0:
        print("No Negative value allowed")
expo()





    
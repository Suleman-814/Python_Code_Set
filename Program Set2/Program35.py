#WAP to find factorial of number using function in python?

def fact(n):
    if  n==0 or n==1 :
        return n
    else:
        return n*fact(n-1)
print("Enter a number whose factorial is to be performed : ")
Number= int(input())
if Number<0:
    print("Factorial not possible ")
else:
    print("Factorial of", {Number}, "is", fact(Number))


    
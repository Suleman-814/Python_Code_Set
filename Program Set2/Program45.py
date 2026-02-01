#WAP to Handle ValueError Using Exception Handling

try:
    h=int(input("enter a number"))
    print(h)
except ValueError:
    print("Some error!")

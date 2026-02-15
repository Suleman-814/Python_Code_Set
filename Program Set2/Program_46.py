#WAP to Accept Integer Input Using Exception Handling in a Loop

while True:
    try:
        h = int(input("Enter a valid number: "))
        print(h)
        continue
    except ValueError:
        print("Some error! Please enter a valid number.")
        break


#WAP to Read Numbers add to list and print list when Zero Input entered.

numbers = []

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        print("0 is not allowed. Program stopped.")
        break
    else:
        numbers.append(num)
        print("Number added:", num)


print("Final list:", numbers)

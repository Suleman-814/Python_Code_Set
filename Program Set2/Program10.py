WAP to give disscount on items purchased

p= int(input("Enter the price of item : "))
if p<0:
    print("no negative")
    if p>2000:
        discount= 0.2
        final_price = p - (discount * p)
        print("Final price : ",final_price)
    elif p>=1000:
        discount= 0.1
        final_price = p - (discount * p)
        print("Final price : ",final_price)
    elif p<1000:
        amount=1000-p
        print(f"you need to purchase ${amount} more ", amount)
    else:

        print("no disscount")

price=float(input("Enter The Bike Price Before Tax :"))
if price>0:
   
    if price>=100000:
        Tax_P="15%"
        Tax= (price*0.15)
        Amount=Tax+price
        print("Tax percentage is:", Tax_P)
        print("Total Amount of Tax:",Tax)
        print("Total Amount of Bike to be Paid after Tax :",Amount)
    elif price>=50000 and price<100000:
        Tax_P="10%"
        Tax= (price*0.1)
        Amount=Tax+price
        print("Tax percentage is:", Tax_P)
        print("Total Amount of Tax:",Tax)
        print("Total Amount of Bike to be Paid after Tax :",Amount)
    elif price<50000:
        Tax_P="5%"
        Tax= (price*0.05)
        Amount=Tax+price
        print("Tax percentage is:", Tax_P)
        print("Total Amount of Tax:",Tax)
        print("Total Amount of Bike to be Paid after Tax :",Amount)
else:
    print("Enter a valid price")
    print("No negative sign or zero")
    

    

    


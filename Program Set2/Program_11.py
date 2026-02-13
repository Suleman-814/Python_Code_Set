
ser= float(input("Enter the time period of service :"))
sal= float(input("Enter the salary: "))
if ser>10:
    b=0.1
    bn_Sal = sal + (b * sal)
    net_b= sal*b
    print(" bonus amount is: ", net_b)
    print("Final Salary : ",bn_Sal)
elif ser>=6 and ser<=10:
    b=0.08
    bn_Sal = sal + (b * sal)
    net_b= sal*b
    print(" bonus amount is: ", net_b)
    print("Final Salary : ",bn_Sal)
elif ser<6:
    b=0.05
    bn_Sal = sal + (b * sal)
    net_b= sal*b
    print(" bonus amount is: ", net_b)
    print("Final Salary : ",bn_Sal)
else:
    print("Success! comes to those who work hard")


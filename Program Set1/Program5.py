#Program to demonstrate  working of  tuples in python.

#Create a tuples
TupleMNC1=("Google","Meta","Microsoft","IBM","Oracle","SAP")
TupleMNC2=("Cisco","Crowdstrike","Palo Alto Network","Fortinet","Rapid7")
TupleMNC3=("Samsung", "Amazon", "HP", "Alphabet")

#Accessing a tuples
print(TupleMNC1)
print(TupleMNC2)
print(TupleMNC3)

#accessing tuples with indexing
print("Indexing1 :" ,TupleMNC1[-2])
print("Indexing2 :" ,TupleMNC2[1])
print("Indexing3 :" ,TupleMNC3[3])

#Slicing of tuples
print("sliced tuple1 : ", TupleMNC1[1:-2])
print("sliced tuple2 : ", TupleMNC2[0:3])
print("sliced tuple3 : ", TupleMNC3[1:3])

#Length of tuples
print("Length of tuple1 : ", len(TupleMNC1))
print("Length of tuple2 : ", len(TupleMNC2))
print("Length of tuple3 : ", len(TupleMNC3))

#Deleting a tuple
del(TupleMNC3)

#Concatenating a tuples
print("TupleWorldsMNC : ", TupleMNC1+TupleMNC2)

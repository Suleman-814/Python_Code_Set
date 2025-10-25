# Program to demonstrate working with dictionaries in python

#Creating a dictionary
DictionaryPython = {
"List":"A list is an ordered and changeable,collection ",
"Set" :"A set is an unordered and unchangeable,collection ",
}
print("Python values : ")
for key, value in DictionaryPython.items():
    print(f"{key}:{value}")

#Accessing values in dictionary
Choice= str(input("Accessing individual values : "))
print(DictionaryPython[Choice])

#Accessing key values
print("Accessing Keys : ",list(DictionaryPython.keys()))

#Updating a dictionary
DictionaryPython["Python"]="Python is an programing language"
print(DictionaryPython)

#Poping a kay values
DictionaryPython.pop("Python")
print(DictionaryPython)

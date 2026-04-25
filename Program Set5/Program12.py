n= (2,3,4)
from functools import reduce
def expo(a,b):
    return a**b
c5= reduce(expo, n)
print(c5)
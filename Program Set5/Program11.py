n= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
from functools import reduce
def div(a,b):
    return a/b
c4= reduce(div, n)
print(c4)
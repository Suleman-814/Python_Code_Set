n= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
from functools import reduce
def fdiv(a,b):
    return a//b
c6= reduce(fdiv, n)
print(c6)
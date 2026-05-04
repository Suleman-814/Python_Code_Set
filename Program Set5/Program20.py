def square():
    s=1**2
    yield s
    s= 2**2
    yield s
    s= 3**2
    yield s
    s= 4**2
    yield s
    s= 5**2
    yield s
    s= 6**2
    yield s
    s= 7**2
    yield s
    s= 8**2
    yield s
    s= 9**2
    yield s
    s= 10**2
    yield s   
result= square()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

    
def myfun1(n):
    return lambda a: a * n 
                # a: 15, n: 5
doublethevalue = myfun1(2)
triplethevalue = myfun1(3)
print(doublethevalue(11))
print(triplethevalue(11))
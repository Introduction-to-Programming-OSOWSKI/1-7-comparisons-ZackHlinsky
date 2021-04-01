def greaterThan(x, y):
    if abs(x) > abs(y):
        return(True)
    else: 
        return(False)
def lessThan(x, y):
    if abs(x) < abs(y):
        return(True)
    else: 
        return(False)
def equalTo(x, y):
    if abs(x) == abs(y):
        return(True)
    else:
        return(False)
def greaterOrEqual(x, y):
    if abs(x) >= abs(y):
        return(True)
    else:
        return(False)
def lessOrEqual(x, y):
    if abs(x) <= abs(y):
        return(True)
    else:
        return(False)

print(greaterThan(5, 6))
print(greaterThan(6, 5))
print(lessThan(6, 5))
print(lessThan(5, 6))
print(equalTo(5, 6))
print(equalTo(5, 5))
print(greaterOrEqual(5, 6))
print(greaterOrEqual(5, 5))
print(lessOrEqual(6, 5))
print(lessOrEqual(5, 5))
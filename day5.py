def is_(val1, val2):
    if id(val1) == id(val2):
        if val1 == val2:
            return True
    return False

a = [1, 2, 3]

b = [2, 3]

print(is_(a, b))

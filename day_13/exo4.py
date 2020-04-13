def is_prime(var):
    for i in range(2, var):
        if var % i == 0:
            return False
    return True
  

print(is_prime(3))
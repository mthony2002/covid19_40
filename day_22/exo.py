numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

def sumMap(m):
  s =0
  for e in m:
    s += int(e)
  return s

mapSum = map(sumMap,numbers)

print(next(mapSum))
print(next(mapSum))

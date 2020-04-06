for elem in range(1,101):
  if elem%3 == 0 and elem%5 ==0:
    print ("Fizz Buzz")
  elif elem%3 == 0:
    print ("Fizz")
  elif elem%5 == 0:
    print( "Buzz")
  else:
    print(elem)

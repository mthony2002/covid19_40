
def divide(a, b):
  try:
	  print(a / b)
  except ZeroDivisionError as z:
    print(f'Error: {type(z)}')
  except ArithmeticError as a:
    print(f'Error: {type(a)}')
  except TypeError as t:
    print(f'Error: {type(t)}')
  

print(divide(1,0))

print(divide(1,'0'))






try:
  nbr = int(input('Please enter a number [1 -10]: '))
except ValueError as ex:
  print(f'Error: {ex}')
else:
  try:
    if nbr not in range(0,11):
      raise print(f'value must be in  range [1 - 10]')
    print (nbr)
  except Exception as e:
    print(f'Error : {e}' )
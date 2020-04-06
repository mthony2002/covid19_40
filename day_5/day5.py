def is_(val1, val2):
    if id(val1) == id(val2):
        if val1 == val2:
            return True
    return False


a = [1, 2, 3]

b = [2, 3]

print(is_(a, b))

'-===================================='

name = input('Your name :')
hWg = int(input('Hourly wage:'))
wk = int(input('Hour Worked :'))
over = 0 
if wk > 40 :
  overWg = (.1 * hWg) + hWg
  overWk = wk - 40 
  over = overWg * overWk
  pay = ( 40 * hWg) + over 
  print(f'the employee is due some additional pay, as well as the amount due is : {pay}')
else:
  pay = (hWg * wk) + over 
  print(f'The amount due is : {pay}')


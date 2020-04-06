employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

def pay(name,wk,hWg ):
    over = 0  
    if wk > 40 :
      overWg = (.1 * hWg) + hWg
      overWk = wk - 40 
      over = overWg * overWk
      pay = ( 40 * hWg) + over 
      print(f'The employee {name} is due some additional pay, as well as the amount due is : ${pay}')
    else:
      pay = (hWg * wk) + over 
      print(f'The amount due to employee {name} is : ${pay}')

for empl in employees:
  pay(empl[0],empl[1],empl[2])

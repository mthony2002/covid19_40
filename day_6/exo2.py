employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

def getAvg ():
   tot = 0
   for elem in employees:
      tot += elem[2]
   return (tot/ len(employees))
  
def pay_avg(name,wk,hWg ):
    avg = getAvg()
    over = 0  
    if hWg > avg :
      if wk > 40 :
        overWg = (.1 * hWg) + hWg
        overWk = wk - 40 
        pay = ( 40 * hWg) + overWg * overWk
        print(f'The employee {name} is due some additional pay, as well as the amount due is : ${pay}')
      else:
        pay = (hWg * wk) + over 
        print(f'The amount due to employee {name} is : ${pay}')

for empl in employees:
  pay_avg(empl[0],empl[1],empl[2])

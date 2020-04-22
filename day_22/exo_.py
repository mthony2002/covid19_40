from itertools import cycle

empl =cycle(['employe A','employe B','employe C'])
week = cycle(['lun','mar','mer','jeu','ven','sam','dim'])

for i in range(1,31):
  print(f'{next(empl)} will close {next(week)} {i}.')

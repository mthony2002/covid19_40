series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]

def print_show_info(dictVar):
  temp =[]
  for value in dictVar.values():
    temp.append(value)
  title, season, initial = temp
  print (f'{title} ({initial}) - {season} seasons.') 


for serie in series:
  print_show_info(serie)
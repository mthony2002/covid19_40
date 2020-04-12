tv_show = {
 	"title": "Breaking Bad",
 	"seasons": 5,
 	"initial_release": 2008
   }

def print_show_info(dictVar):
  temp =[]
  for value in dictVar.values():
    temp.append(value)
  title, season, initial = temp
  print (f'{title} ({initial}) - {season} seasons.') 

print_show_info(tv_show)
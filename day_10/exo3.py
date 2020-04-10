

mydict = {}

(mydict['album_name'],mydict['artist'],mydict['year_of_release'],mydict['track_list']) = (
 	"The Dark Side of the Moon",
 	"Pink Floyd",
 	1973,
 	(
 		"Speak to Me",
 		"Breathe",
 		"On the Run",
 		"Time",
 		"The Great Gig in the Sky",
 		"Money",
 		"Us and Them",
 		"Any Colour You Like",
 		"Brain Damage",
 		"Eclipse"
 	)
 )

for key, value in mydict.items():
  print(f'{key} : {value}')


print('\n\n')
del mydict['year_of_release']
del mydict['track_list']
mydict.update({'year_of_release': 'March 1st, 1973'})


for key, value in mydict.items():
  print(f'{key} : {value}')
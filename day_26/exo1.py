from collections import namedtuple

Movie = namedtuple('Movie',[ 'title', 'director' ,'year', 'budget'])

title = input('Enter the title of the movie :')
director =input('Enter the director of the movie :')
year = input('Enter the year of the movie :')
budget =input('Enter the budget of the movie :')


oneMovie =  Movie(title,director,year,budget)





movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]



def avgBdgt(movies):
  """
  Average budget of all movies
  """
  avg = 0
  for movie in movies:
    avg += movie[1]
  return avg/len(movies)



def higherThanAvgBdgt(movies):
  count = 0 
  for movie in movies:
    avg = avgBdgt(movies)
    if movie[1] > avg:
      print(f" - {movie[0]} is much ${(movie[1] - avg)} higher than the average the movie's budget was.")  
      count += 1
  return count


print( f"\n{higherThanAvgBdgt(movies)} movies spent more than the average movie budget.")
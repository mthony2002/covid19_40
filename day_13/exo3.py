def tupleToDict(var):
  name,nationality,age = var
  return {
    'name': name ,
    'nationality':nationality,
    'age':age
  }

print(tupleToDict(("Tom Hardy", "English", 42)))
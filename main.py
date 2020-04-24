def itemgetter(collection, identifier):
  try:
	   r = collection[identifier]
  except (IndexError, KeyError,TypeError)  as e:
    err= f" Collection: {collection} - Identifier: {identifier}  -  TypeError: {e} \n"
    print(err)
    with open('log.txt', 'a') as f:
      f.write( err)
  else:
    return r

l = [1,2]

print(itemgetter(l,'4'))
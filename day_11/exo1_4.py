mySet = set()
mySet.update(["carrot", "lettuce", "broccoli"])

sndSet = set() 
sndSet.add("onion")
sndSet.add("lettuce")
sndSet.add("potato")

unionSet = mySet.union(sndSet)
symSet =  mySet.symmetric_difference(sndSet)
interSet =  mySet.intersection(sndSet)

print(f'- Union Set : {unionSet}')  
print(f'- symetric difference Set : {symSet}')  
print(f'- Intersection Set : {interSet}')  

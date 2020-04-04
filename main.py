lst = [('movie1','director1',2000)]

name = input('Your name :')
direct = input('Director name:')
year = input('the year :')
nw = (name,direct,year)
print(f'name : {nw[0]} and year : {nw[1]} ')
lst.append(nw)
for m in lst:
  print(f'name : {m[0]} and year : {m[1]}')
del lst[0]
print(lst)

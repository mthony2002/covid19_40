
oldList = list(range(10))

tmpList =[]
for i in oldList: 
  tmpList.append(str(i))

res = " | ".join(tmpList)

print(res)
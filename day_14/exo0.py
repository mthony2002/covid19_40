
with open('iris.csv','r') as f:
  fContent =  f.readlines()
myList=[]
header = fContent[0].split(',')
for e in range(1 , len(fContent)):
  myList.append(dict(zip(header,fContent[e].strip().split(','))))

  
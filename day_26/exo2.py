from collections import defaultdict

d = defaultdict(int)

print(d.items)

myStr = input('Please enter a String')

for i in myStr:
  d[i] += 1



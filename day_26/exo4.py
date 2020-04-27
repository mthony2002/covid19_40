from functools import partial

popen = partial(open,mode='r')

with popen('log.txt') as f:
  print(f.readlines())

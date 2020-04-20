try:
  with open('data.txt','r') as f:
    print(f.readline())
except FileNotFoundError:
  print('File doesnt exist !')
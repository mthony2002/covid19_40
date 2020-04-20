userInput = input('Enter a list of grades separated by commas : ')

toList = userInput.split(',')

try:
  toList  = [ int(item) for item in toList ]
except:
  print('The value entered cannot be converted !')

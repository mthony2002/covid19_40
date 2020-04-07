word = input("Enter a word :").strip()

print(f'The length of ur input is : {len(word)}.')

allText = input("Enter a text :").strip()
count = 0
listWord = allText.split(' ')

for word in allText:
  if word != '':
    count += 1

print(f'The number of words in ur text : {len(listWord)}.')

print(f'The number of characters in ur text : {count}.')

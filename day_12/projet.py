# add a book to their reading list by providing a book title, an author's name, and a year of publication.

readingList = []

def add():
  name=input('Enter the book name :').rstrip()
  author=input('Enter the author name :').rstrip()
  year= input('Enter the year :').rstrip()
  readingList.append((name,author,year))

def listBook():
  if len(readingList) != 0 :
    for name, author, year in readingList:
      print (f' - {name} written by {author}, {year}')
  else:
    print(' No books !')
  print()
def quit():
  print('Bye - Bye !')
  
def menu():
 
  print("- (a) to add a book. ")
  print("- (l) to list all the books.")
  print("- (q) to quit the program. ")
  print()
  options = input('Please choose your option :')
  print()
  return options

def load():
  opt = menu()
  while opt != 'q':
    if opt == 'a':
      add()
    elif opt =='l':
      listBook()
    opt = menu()
  
print("welcome ")
print()
load()

# Some kind of do while
valid = False
card = ''
while valid == False or card == '':
  card =  input('Enter a valid card number :')
  print(card.isdigit())
  valid = True if len(card) == 16 and card.isdigit()  else False 

# Remove the last digit
sum_lastD = int(card[-1])
card_L = card[0:-1]

print(card_L)
# Reverse the remaining digits  
reverse_Card = card_L[::-1]
card_F = []
# Double digits at even indices 
for idx in range(len(reverse_Card)):
  if idx%2 == 0:
    tmp = int(reverse_Card[idx])
    if (tmp * 2) > 9:
      card_F.append((tmp * 2) - 9) # Subtract 9 if over 9
    else: 
      card_F.append(tmp * 2)
  else:
    card_F.append(reverse_Card[idx])

for elem in card_F:
   sum_lastD += int(elem)

if sum_lastD%10 == 0 :
  print('card valid !')
else:
  print('card not valid !')



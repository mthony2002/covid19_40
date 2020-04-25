from random import sample

lst1 = sample([*range(1,101)],15)
lst2 = sample([*range(1,101)],15)
lst3 = sample([*range(1,101)],15)


slst1 = sorted(lst1, reverse=True)[10:]
slst2 = sorted(lst2, reverse=True)[10:]
slst3 = sorted(lst3, reverse=True)[10:]

print([slst1,slst2,slst3])
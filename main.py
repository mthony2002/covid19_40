from random import sample

lst1 = sample([*range(1,101)],15)
lst2 = sample([*range(1,101)],15)
lst3 = sample([*range(1,101)],15)


slst1 = sorted(lst1, reverse=True)[10:]
slst2 = sorted(lst2, reverse=True)[10:]
slst3 = sorted(lst3, reverse=True)[10:]


print([slst1,slst2,slst3])

# import random

# population = range(1, 101)
# numbers = [random.sample(population, 15) for _ in range(3)]

# for number_set in numbers:
# 	number_set.sort(reverse=True)
# 	del number_set[5:]

# print(numbers)


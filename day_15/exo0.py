names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = []

# for name, age in zip(names, ages):
# 	person_data = (name.title(), age)
# 	people.append(person_data)

people = [(name.title(), age) for name, age in zip(names, ages)]


print (people)



import itertools

for elem in flower_names:
    print((elem,))

for elem in itertools.combinations(flower_names, 2):
    print(elem)

for elem in itertools.combinations(flower_names, 3):
    print(elem)

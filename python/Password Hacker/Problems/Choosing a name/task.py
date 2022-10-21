import itertools

for name in itertools.product(first_names, middle_names):
    out = ' '.join(name)
    print(out)

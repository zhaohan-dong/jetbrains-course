def tallest_people(**kwargs):
    tallest = {}
    height = 0
    for k, v in kwargs.items():
        if v > height:
            tallest = {}
            tallest.update({k: v})
            height = v
        elif v == height:
            tallest.update({k: v})
    for k, v in sorted(tallest.items()):
        print(k + ' :', v)

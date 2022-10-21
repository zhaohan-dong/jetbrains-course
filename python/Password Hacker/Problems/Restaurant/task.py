import itertools

for comb, price in zip(itertools.product(main_courses, desserts, drinks),
                       itertools.product(price_main_courses, price_desserts, price_drinks)):
    total = price[0] + price[1] + price[2]
    out = ' '.join(comb)
    if total <= 30:
        print(out, str(total))

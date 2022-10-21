# work with the variable `child`
if type(child) == Drinks:
    print('Drinks')
if type(child) == Pastry:
    print('Pastry')
if isinstance(child, Sweets):
    print('Sweets')
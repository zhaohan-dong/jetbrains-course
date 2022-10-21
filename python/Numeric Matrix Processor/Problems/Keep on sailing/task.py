# our class Ship
class Ship:
    def __init__(self, name, capacity, dest):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.dest = dest

    # the old sail method that you need to rewrite
    def sail(self):
        print("The {} has sailed for {}!".format(self.name, self.dest))

city = input()
black_pearl = Ship("Black Pearl", 800, city)
black_pearl.sail()
iris = {}

def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    new_species = {id_n: {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}}
    for k, v in kwargs.items():
        new_species[id_n].update({k: v})
    iris.update(new_species)

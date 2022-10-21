# read animals.txt
animals = open('animals.txt', 'r')
# and write animals_new.txt
animals_new = open('animals_new.txt', 'w+')
animal_list = animals.readlines()
animal_list = [elem.replace('\n', '') for elem in animal_list]
animals_new.write(' '.join(animal_list))
animals.close()
animals_new.close()

# put your python code here
minimum = ['', 10000]
maximum = ['', 0]
for key, value in test_dict.items():
    if value < minimum[1]:
        minimum = [key, value]
    elif value > maximum[1]:
        maximum = [key, value]
print("min: " + minimum[0])
print("max: " + maximum[0])

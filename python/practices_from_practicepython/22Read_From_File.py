#!/usr/bin/python3

#partially done


def main():
    with open("Training_01.txt", "r") as file_cat:
        line = file_cat.readline()
        count_file = open("Training_01_count.txt", "w+")
        if line:
            line = line.split("/")
        else:
            print("Error Input File")
        count_c = 0  # total category count
        while line:
            category = line[1]  # category is the first directory
            # count in same category
            subcatdict = {}  # create dictionary for subcat name and count
            print(line[2])
            while line[1] == category:
                subcategory = line[2]  # subcategory is second directory
                count_c += 1
                subcatdict.update({subcategory: 0})
                # count in same subcategory
                print(line[2])
                while line[1] == category and line[2] == subcategory:
                    # line[1] == category prevents reading next category with same subcat name
                    subcatdict[subcategory] += 1
                    line = file_cat.readline()
                    line.split("/")
            count_s = 0
            for k, v in subcatdict.items():
                count_s = count_s + v
            count_file.write("\n{}".format(category))
            count_file.write("(Total {}, Subcategories {}):".format(v, len(subcatdict)))
            count_c += 1
            line = file_cat.readline()
            line = line.split("/")
        count_file.write("Total {} categories".format(count_c))
        x = 0
        for i in open("Training_01.txt"):
            x += 1
        count_file.write("Total {} items".format(x))
        file_cat.close()
        count_file.close()


if __name__ == '__main__':
    counter_dict = {}
    with open('Training_01.txt') as f:
        line = f.readline()
        while line:
            line = line[3:-26]
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = f.readline()

    print(counter_dict)

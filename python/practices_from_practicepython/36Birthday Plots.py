#!/usr/bin/python3


import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

def main():


    with open("birthday.json", "r") as f:
        bd_dict = json.load(f)
        num_to_string = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        months = []
        for name, birthday_str in bd_dict.items():
            month = int(birthday_str.split("-")[1])
            months.append(num_to_string[month])
        output_file("plot.html")
        x = [Counter(months).keys()]
        y = [Counter(months).values()]
        p = figure()
        p.vbar(x=x, top=y, width=0.5)
        show(p)


if __name__ == '__main__':
    main()
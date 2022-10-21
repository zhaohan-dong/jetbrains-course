def average_mark():
    total = 0
    marks = [int(elem) for elem in input().split(" ")]
    for mark in marks:
        total = total + mark
    result = round(total / len(marks), 1)
    print(result)

average_mark()

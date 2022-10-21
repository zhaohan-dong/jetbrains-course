#!/usr/bin/python3


def max_list(int_list):
    if len(int_list) == 1:
        return int_list[0]
    else:
        if int_list[0] > max_list(int_list[1:]):
            return int_list[0]
        else:
            return max_list(int_list[1:])


def main():
    print(max_list([1, 3, 5, 7, 9, 10, 1]))

if __name__ == '__main__':
    main()
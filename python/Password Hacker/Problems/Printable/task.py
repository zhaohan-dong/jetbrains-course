code = int(input())
if code > 126 or code < 32:
    print('False')
else:
    print(chr(code))

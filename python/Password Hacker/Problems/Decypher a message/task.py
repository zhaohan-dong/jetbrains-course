line1 = input()
line2 = sum((int(input())).to_bytes(2, byteorder='little'))
decoded = ''
for char in line1:
    decoded += chr(ord(char) + line2)
print(decoded)

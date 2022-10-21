word1 = input()
word2 = input()
out = ""
for let1, let2 in zip(word1, word2):
    out += let1 + let2
print(out)

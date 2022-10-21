vowels = 'aeiou'
# create your list here
word = input()
pick = [elem for elem in word if elem in vowels]
print(pick)

card1 = input()
card2 = input()
card3 = input()
card4 = input()
card5 = input()
card6 = input()
cardval = {'Ace':14, '2':2, '3':3,
           '4':4, '5':5, '6':6,
           '7':7, '8':8, '9':9,
           '10':10, 'Jack':11, 'Queen':12,
           'King':13}
print((cardval[card1]+cardval[card2]+cardval[card3]+cardval[card4]+
      cardval[card5]+cardval[card6])/6)
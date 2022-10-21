#!/usr/bin/python3


class parentheses_val:
    def verify(self, string):
        val = True
        par_dict = {"{": "}", "[": "]", "(": ")"}
        string = list(string)
        if len(string) % 2 != 0 or len(string) < 1:
            return False
        while val and len(string) > 0:
            val = False
            for i in range(len(string)):
                if string[i + 1] == par_dict[string[i]]:
                    string.pop(i)
                    string.pop(i)   #pop [i] because [i+1] now is [i]
                    val = True
                    break
                break
        return val

print(parentheses_val().verify(""))
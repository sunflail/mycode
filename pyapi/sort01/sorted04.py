#!/usr/bin/env python3

simpsons = [ ('Moe', "?"), ('Otto', '?'), ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34), ('Lional', 10) ]

def hasAge(character):
    if type(character[1]) == int:
        return character[1]
    else:
        return 1 #adds age of 1, placing them at the front

sortByAge = sorted(simpsons, key= hasAge)

print(simpsons)
print(sortByAge)

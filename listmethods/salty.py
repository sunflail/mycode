#!/usr/bin/env python3
icecream= ["flavors", "salty"]

icecream.append(int("99")) #reduandant recasting, could just append(99)
print(type(icecream[2]))
name = input("Enter your name: ")

print(f"{icecream[2]} {icecream[0]}, and {name} chooses to be {icecream[1]}")

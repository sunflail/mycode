#!/usr/bin/env python3
star = "*"
up_count = 1
down_count = 4

for vert in range(10):
    if up_count <= 5:
        print(star*up_count)
        up_count += 1
    elif down_count > 0:
        print(star*down_count)
        down_count -= 1

art = {1:"*", 2:"**", 3:"***", 4:"****", 5:"*****", 6:"****", 7:"***", 8:"**", 9:"*"}

for key in art:
    print(art[key])

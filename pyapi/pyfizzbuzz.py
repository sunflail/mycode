#!/usr/bin/env python3

# print from 1 to 100 on new line
# multiple of 3, print fizz
# multiple of 5, print buzz
# numbers multiples of 3 and 5, print fizzbuzz instead of number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

result = ["FizzBuzz" if (i % 15 == 0) else "Fizz" if (i % 3 == 0) else "Buzz" if (i % 5 == 0) else i for i in range(1,101)]
print(result)

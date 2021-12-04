"""
This module implements fizzbuzz
for multiples of 3, fizz is printed.
for multiples of 5, buzz is printed.
for multiples of both 3 and 5, fizzbuzz is printed.
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)

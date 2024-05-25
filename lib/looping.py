#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 11
    while i>1:
        i-= 1
        print(i)
    print("Happy New Year!")


def square_integers(int_list):
    squares = [num ** 2 for num in int_list ]
    return squares
square_integers([1,2,3,4,5,-1,-2,-3,-4,-5])
#square_integers([-1,-2,-3,-4,-5])

def fizzbuzz():
    # code goes here!
    b = 0
    while b < 100:
        b += 1
        def fb_num(b):
            if b % 3==0 and b% 5 == 0:
                return "FizzBuzz"
            elif b % 5 == 0:
                return "Buzz"
            elif b % 3 == 0:
                return "Fizz"
            else:
                return b
        print(fb_num(b))
        
fizzbuzz()   

#!/bin/python3

import sys

t = int(input().strip())
def summer(x,a):
    return int((x * (2*a + (x-1)*a)>>1))

for a0 in range(t):
    sum= 0
    n = int(input().strip())  
    sum = summer(int((n-1)/3),3) + summer(int((n-1)/5),5) - summer(int((n-1)/15),15) 
    print(sum)

# Notes :-
# While using Python3. I've already converted the complexity to an O(1) but I'm still getting the "wrong answer" with Test Cases 2 and 3:

# When I divide integers in python 3, the answer is converted automatically to a float. Becuase Test Cases 2 and 3 involve very large numbers, when I convert back to integer, there will be a huge rounding error and your answers will be wrong.

# This is the issue I had to resolve. Luckily for me, my only division was a divide by two so I converted it to a bitwise right-shift.

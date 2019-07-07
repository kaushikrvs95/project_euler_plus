#!/bin/python3
'''
The largest prime factor for a number can be obtained by performing a reccursive approach where we can iterate from a range of
3 -> √N to get the prime factors because beyond √N there wouldnt be any number that can exactly divide N. Hence we try to reduce
the computational complexity of the algorithm.
'''


import sys
import math

# Function that iterates from 3 to √N to checj if the number is exactly divisible in the # given range. 
def pf_checker(n):
    for i in range(3,int(math.ceil(n**0.5))+1,2):
        if n%i == 0:
            return int(n/i)
    return int(n)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
  # Checks if the number is even and filters the number till it is reduced to odd factors
    while n%2 == 0:
        n = int(n/2)
    if n == 1:
        print(2)
    else:
  # After filtering out the even factors, we look for all the odd prime factors using the 
  # Pf_checker() function. We do recursion until the number is no longer divisible and 
  # concluding that it is the prime factor.
        pf1=0
        pf2=n
        while (pf1 != pf2):
            pf1 = pf_checker(pf2)
            pf2 = pf_checker(pf1)

    print(pf2)

#!/bin/python3

'''
Problem Approach :-
Fibonacci sequence F(n) = F(n-1) + F(n-2)
The target is to filter out all the non-even numbers in the sequence and then find the sum of all remaining even numbers.

1. Observe the sequence; and find a pattern
    We see that every third number is an even number
2. Now, figure out a formula that fits this pattern.
    Since we already have an existing formula we can decompose it as per our needs;
    F(n) = F(n-1) + F(n-2)
    F(n) = F(n-2) + F(n-3) + F(n-2)
    F(n) = 2F(n-2) + F(n-3)     ------- (1) We see that the 3rd number in the pattern of
    n-2, n-1, n can be even if F(n-3) is even and since we know 2F(n-2) is always even.
    This will work but we still pick every number in the Fibonacci series; hence it is 
    no different than the brute force algorithm. We should decompose the equation in 
    such a way that we can jump to the conclusion using only even numbers in the 
    sequence.

    F(n) = 3F(n-3) + 2F(n-4)
    F(n) = 3F(n-3) + 2F(n-5) + 2F(n-6)
    From eq(1); F(n-3) = 2F(n-5) + F(n-6) ---> 2F(n-5) = F(n-3) - F(n-6)
    F(n) = 4F(n-3) + F(n-6)

    This equation gives us every 3rd number in the sequence; hence we can run through
    all the even numbers.
'''

import sys


t = int(input().strip())

def summer(num_1,num_2):
        return 4*num_2 + num_1 

for a0 in range(t):
    n = int(input().strip())
    num_1 = num_3 = 0
    num_2 = 2
    total_1 = 2
    i = 1
    while(i):
        total_1 += num_3
        num_3 = summer(num_1,num_2)
        num_1 = num_2
        num_2 = num_3
        if num_3 <= n:
            pass
        else:
            print(total_1)
            i = 0
            

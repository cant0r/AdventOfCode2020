#!/usr/bin/env python3

import math

INPUT = "./input.txt"


def binary_op(_input):
    low = 0
    high = 2**len(_input) -1


    for c in _input:
        if c in ['B', 'R']:
            low += (high-low +1) // 2 
        else:
            high -= (high-low) // 2
    
    return min(low,high)

def first_part():
    max_id = 0
    with open(INPUT, 'r') as f:
        for line in f:
            row = binary_op(line[:7])
            col = binary_op(line[7:].rstrip())
            max_id = max(max_id,row*8+col)
    print(max_id)

def second_part():
    seats = set()
    with open(INPUT,'r') as f:
        for line in f:
            row = binary_op(line[:7])
            col = binary_op(line[7:-1])
            seats.add(row*8+col)
    for i in range(128):
        for j in range(8):
            if i*8+j not in seats:
                print(i*8+j)


def main():
    first_part()
    second_part()
    

if __name__ == "__main__":
    main()
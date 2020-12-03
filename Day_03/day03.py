#!/usr/bin/env python3

import math

INPUT = "./input.txt"

def parts():
    trees = {}
    with open(INPUT,'r') as f:
        first_line = f.readline()
        length = len(first_line)-1
        position_1_odd = 0
        position_1_even = 0
        position_3 = 0
        position_5 = 0
        position_7 = 0

        for i,line in enumerate(f):
            position_1_odd += 1
            position_1_even = position_1_even + 1 if (i+1) % 2 == 0 else position_1_even
            position_3 += 3
            position_5 += 5
            position_7 += 7
            if line[position_1_odd % length] == "#":                
                trees['1_odd'] = trees.get('1_odd', 0) + 1

            if (i+1) % 2 == 0 and line[position_1_even % length] == "#":                
                trees['1_even'] = trees.get('1_even', 0) + 1
            
            if line[position_3 % length] == "#":                
                trees['3'] = trees.get('3', 0) + 1

            if line[position_5 % length] == "#":                
                trees['5'] = trees.get('5', 0) + 1
            if line[position_7 % length] == "#":                
                trees['7'] = trees.get('7', 0) + 1

    print(trees['3'])
    print(math.prod(trees.values()))


def main():
    parts()

if __name__ == "__main__":
    main()
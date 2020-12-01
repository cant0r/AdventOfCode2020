#!/usr/bin/env python3

INPUT = "./input.txt"
SUM = 2020


def first_part():
    number_set = set()
    with open(INPUT,"r") as f:
        for line in f:
            n = int(line)
            if n in number_set:
                print(n*(SUM-n))
                return
            number_set.add(SUM-n)    

def second_part():
    dumpster = set()
    partial_sums = {}
    with open(INPUT,"r") as f:
        for line in f:
            n = int(line)
            if n in partial_sums:                
                print(n*partial_sums[n])
                return
            for m in dumpster:
                partial_sums[SUM-(n+m)] = n*m
            dumpster.add(n)

def main():
    first_part()
    second_part()

if __name__ == "__main__":
    main()
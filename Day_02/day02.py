#!/usr/bin/env python3

INPUT = "./input.txt"

def first_part():
    valid_passwords = 0
    with open(INPUT,"r") as f:        
        for line in f:
            freq_table = {}
            l = line.split(':')
            password = l[1]
            rules = l[0].split()
            min = int(rules[0].split('-')[0])
            max = int(rules[0].split('-')[1])
            key_char = rules[1]

            for c in password:
                freq_table[c] = freq_table.get(c,0) + 1
            if freq_table.get(key_char,0) in range(min,max+1):
                valid_passwords += 1

    print(valid_passwords)

def second_part():
    valid_passwords = 0
    with open(INPUT,'r') as f:
        for line in f:        
            l = line.split(':')
            password = l[1]
            rules = l[0].split()
            min = int(rules[0].split('-')[0])
            max = int(rules[0].split('-')[1])
            key_char = rules[1]
            found = False

            for i,c in enumerate(password):            
                if i == min and c == key_char:
                    found = True
                if i == max and c == key_char:
                    if found:
                        found = False
                    else:
                        found = True
            if found:
                valid_passwords += 1
    print(valid_passwords)


def main():
    first_part()
    second_part()

if __name__ == "__main__":
    main()
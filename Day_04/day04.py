#!/usr/bin/env python3

import re

INPUT = "./input.txt"

fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def valdiate(passport):    
    for field in fields:
        if field not in passport:
            return False
    return True

def strict_validate_range(value, min, max):
    return value >= min and value <= max

def strict_validate(passport):
    if (byr := passport.get("byr", "0")):
        if not strict_validate_range(int(byr),1920,2002):
            return False
    if (iyr := passport.get("iyr", "0")):
        if not strict_validate_range(int(iyr), 2010,2020):
            return False
    if (eyr := passport.get("eyr", "0")):
        if not strict_validate_range(int(eyr), 2020,2030):
            return False
    if (hgt := passport.get("hgt", "0")):
        if not (hgt.endswith("cm") or hgt.endswith("in")):
            return False
        if hgt.endswith("cm") and not strict_validate_range(int(hgt[:-2]), 150,193):
            return False
        if hgt.endswith("in") and not strict_validate_range(int(hgt[:-2]), 59,76):
            return False
        
 
    if (hcl := passport.get("hcl", "0")):
        if not (len(hcl) == 7 or hcl.startswith("#")) or re.search("^[0-9a-f]{6}$", hcl[1:]) == None:
            return False
    if (ecl := passport.get("ecl", "0")):
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
    if re.search("^[0-9]{9}$",(pid := passport.get("pid", "0"))) == None:
        return False
    return True


def first_part():
    current_passport = {}
    invalid = 0
    total = 0

    with open(INPUT,'r') as f:
        for line in f:
            if len(line) == 1:
                if not valdiate(current_passport):
                    invalid +=1
                total += 1
                current_passport.clear()
            else:
                for entry in line.split():
                    keypair = entry.split(':')
                    current_passport[keypair[0]] = keypair[1]
    print(total-invalid)

def second_part():
    current_passport = {}
    invalid = 0
    total = 0

    with open(INPUT,'r') as f:
        for line in f:
            if len(line) == 1:
                if not strict_validate(current_passport):
                    invalid +=1
                total += 1
                current_passport.clear()
            else:
                for entry in line.split():
                    keypair = entry.split(':')
                    current_passport[keypair[0]] = keypair[1]
    print(total-invalid)



def main():
    first_part()
    second_part()

if __name__ == "__main__":
    main()